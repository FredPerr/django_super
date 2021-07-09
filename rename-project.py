import sys
import os
import pathlib
import fileinput
import re


def _get_project_name():
    manage_file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'manage.py')
    with open(manage_file_path) as file:
        for line in file.readlines():
            if 'DJANGO_SETTINGS_MODULE' in line:
                return line.split("', '")[-1].split('.settings')[0]
    print('**Error** Could not find the name of the project')


def _search_and_replace(file, occurence, replace_by):
    with fileinput.FileInput(file, inplace=True) as file:
        for line in file:
            print(line.replace(occurence, replace_by), end='')


def select_compilers(*args):
    if len(args) < 2 or args[0] not in ('True', 'False') or args[1] not in ('True', 'False'):
        help()
        return

    kval = {
        'USE_TYPESCRIPT': (args[0], 'TypeScript'),
        'USE_SCSS': (args[1], 'SCSS')
    }

    for key, val in kval.items():
        opposite = 'False' if val[0] == 'True' else 'True'
        _search_and_replace(os.path.join(_get_project_name(), 'settings.py'), f'{key} = {opposite}', f'{key} = {val[0]}')
        print(f'{val[1]} compiler is now set to {val[0]}')

def rename_project(*args):
    if len(args) == 0:
        help()
        return
    
    project_name = args[0].lower();
    if (not re.match(r"^([a-z0-9_]{3,20}[^-])$", project_name)):
        sys.exit('Could not change the name of the project.\nThe project name must be lower cased and range from 3 to 20 characters!')
    
    old_project_name = _get_project_name()
    directory_path = pathlib.Path(__file__).parent.absolute()

    to_search = (
        (old_project_name, 'asgi.py'), 
        (old_project_name, 'settings.py'),
        (old_project_name, 'wsgi.py'),
        (old_project_name, 'urls.py'),
        ('manage.py', ),
    )

    for path_sequence in to_search:
        _search_and_replace(os.path.join(directory_path, *path_sequence), old_project_name, project_name)
    
    os.rename(os.path.join(directory_path, old_project_name), os.path.join(directory_path, project_name))

    if (_get_project_name() == project_name):
        print(f"The Django Project has been renamed to '{project_name}' successfully!")
    else:
        print(f"Something went wrong while renaming the project... The action could not be done!")


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('> python rename-project.py [project_name]')
        exit(0)

    name = sys.argv[1]
    rename_project(name)
            


