import sys
import re
import pathlib
from os import path, listdir
import fileinput


def _search_and_replace(file, occurence, replace_by):
    pass


def replace_project_name(name: str):
    name = name.lower();
    if (not re.match(r'[a-z0-9_]{3,20}', name) or '-' in name):
        print('Could not change the name of the project.\nThe project name must be lower cased and range from 3 to 20 characters!')
        return
    
    # change the project name here
    directory_path = pathlib.Path(__file__).parent.absolute()
    file_asgi = path.join(directory_path, 'django_super', 'asgi.py')

    with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace("django_super", name), end='')


    print(f"Project name changed to {name}!\nYou can now rename the main folder of the project to the name of the project.")


if __name__ == "__main__":
    commands = {
        "rename-project": "<project name>",
        "gitinit": "",
        "exit": ""
    }
    cmd_name = sys.argv[1].lower()
    args = sys.argv[2:] if len(sys.argv) > 1 else []
    if (cmd_name not in commands.keys()):
        for k, v in commands.items():
            print(f"{k} {v}")
        print(cmd_name)
        exit(0)

    # Rename project cmd.
    if (cmd_name == list(commands.keys())[0]):
        if (len(args) > 0):
            if (replace_project_name(args[0])):
                input(f"Project renamed sucessfully to {args[0]}.\n")
    elif (cmd_name == list(commands.keys)[-1]):
        exit(0)
