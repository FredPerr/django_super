import fileinput
import sys
import os
import pathlib

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


def use_ts(val):
    if val == 'yes':
        _search_and_replace(os.path.join(_get_project_name(), 'settings.py'), 'USE_TYPESCRIPT = False', 'USE_TYPESCRIPT = True')
        print('You have enabled TypeScript on your project!')
    elif val == 'no':
        _search_and_replace(os.path.join(_get_project_name(), 'settings.py'), 'USE_TYPESCRIPT = True', 'USE_TYPESCRIPT = False')
        print('You have disabled TypeScript on your project!')
    else: print('The answer you have provided does is not one of the following accepted argument: (yes|no)...')


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        use = input('Do you want to use TypeScript in your project ? (yes|no):\n')
    else:
        use = args[0]

    use_ts(use)

