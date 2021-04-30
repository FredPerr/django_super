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


COMMANDS = (
    (select_compilers, "use_typescript use_scss", "Enable or disable the use of TypeScript and/or SCSS. Both argument should be replace by True to activate it and False to desactivate it."),
    (rename_project, "name", "Rename the Django project. The name can contain alphanumerical values and underscores."),
)


def help():
    for cmd in COMMANDS:
        print(cmd[2])
        print(f'==> {cmd[0].__name__.replace("_", "-")} {cmd[1]}\n')


if __name__ == '__main__':

    CMD_NOT_FOUND = 'Make sure to use one of the valid commands below!'

    if len(sys.argv[1:]) == 0:
        help()
        print(CMD_NOT_FOUND)
        exit(0)

    cmd = sys.argv[1].replace('-', "_")
    cmds = [a_tuple[0] for a_tuple in COMMANDS]
    for c in cmds:
        if c.__name__ == cmd:
            c(*sys.argv[2:])
            exit(0)
    print(CMD_NOT_FOUND)
            


