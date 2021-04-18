import sys
import re
import pathlib
import os
import fileinput

def _get_project_name():
    manage_file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'manage.py')
    with open(manage_file_path) as file:
        for line in file.readlines():
            if 'DJANGO_SETTINGS_MODULE' in line:
                return line.split("', '")[-1].split('.settings')[0]

def _search_and_replace(file, occurence, replace_by):
    with fileinput.FileInput(file, inplace=True) as file:
        for line in file:
            print(line.replace(occurence, replace_by), end='')


def rename_project(project_name: str):
    project_name = project_name.lower();
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


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        project_name = input('Choose a name for the project:\n     The name should be lower cased alphanumerical value (underscore include) \n     with length ranging from 3 to 20.\n:')
    else:
        project_name = args[0]
    rename_project(project_name)

    
