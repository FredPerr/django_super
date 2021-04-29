import sys
import os
import pathlib
import fileinput
import re


def _search_and_replace():
    pass


def _get_project_name():
    pass


def select_compilers(*args):
    pass


def rename_project(*args):
    pass


def install(*args):
    pass


COMMANDS = (
    (select_compilers, "use_typescript use_scss", "Enable or disable the use of TypeScript and/or SCSS. Both argument should be replace by True to activate it and False to desactivate it."),
    (rename_project, "name", "Rename the Django project. The name can contain alphanumerical values and underscores."),
    (install, "", "Go through all the different parameters that can be configured with scripts.")
)


def help():
    for cmd in COMMANDS:
        print(cmd[2])
        print(f'==> {cmd[0].__name__.replace("_", "-")} {cmd[1]}\n')


if __name__ == '__main__':

    CMD_NOT_FOUND = 'Make sure to use one of the valid command below!'

    if len(sys.argv[1:]) == 0:
        help()
        print(CMD_NOT_FOUND)
        exit(0)

    cmd = sys.argv[1].replace('-', "_")
    cmds = [a_tuple[0] for a_tuple in COMMANDS]
    for c in cmds:
        if c.__name__ == cmd:
            cmd(sys.argv[:2])
            exit(0)
    print(CMD_NOT_FOUND)
            


