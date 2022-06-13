import re
import pathlib
import os
import getpass
import fileinput

from django.core.management.utils import get_random_secret_key

def get_project_name():
    manage_file_path = os.path.join(pathlib.Path(__file__).parent.absolute(), 'manage.py')
    with open(manage_file_path) as file:
        for line in file.readlines():
            if 'DJANGO_SETTINGS_MODULE' in line:
                return line.split("', '")[-1].split('.settings')[0]
    print('**Error** Could not find the name of the project')

def rename_project(name):
    
    def search_and_replace(file, occurence, replace_by):
        with fileinput.FileInput(file, inplace=True) as file:
            for line in file:
                print(line.replace(occurence, replace_by), end='')

    name = name.lower();
    if (not re.match(r"^([a-z0-9_]{3,20}[^-])$", name)):
        raise ValueError('Could not change the name of the project.\nThe project name must be lower cased and range from 3 to 20 characters!')
    
    old_project_name = get_project_name()
    directory_path = pathlib.Path(__file__).parent.absolute()

    to_search = (
        (old_project_name, 'asgi.py'), 
        (old_project_name, 'settings.py'),
        (old_project_name, 'wsgi.py'),
        (old_project_name, 'urls.py'),
        ('manage.py', ),
    )

    for path_sequence in to_search:
        search_and_replace(os.path.join(directory_path, *path_sequence), old_project_name, name)
    
    os.rename(os.path.join(directory_path, old_project_name), os.path.join(directory_path, name))

    if (get_project_name() == name):
        print(f"The Django Project has been renamed to '{name}' successfully!")
        return name
    else:
        print(f"Something went wrong while renaming the project... The action could not be done!")


def setup():
    print("Please provide the following (password won't be visible)")
    secret_key = get_random_secret_key()
    project_name = input('Project name (if no name providied, it skip this step): ')
    if project_name != '' and rename_project(project_name) is None:
        raise ValueError('The project name could not be set. Make sure to respect the name format of a django project.')
    db_username = input('Database username: ')
    db_password = getpass.getpass('Database user password: ')
    db_host = input('Databse host: ')
    db_port = input('Database port (5432 by default): ')
    if db_port == '':
        db_port = '5432'
    db_name = input('Database name: ')
    gmail_account_address = input('Gmail Account address: ')
    gmail_account_app_code = getpass.getpass('Gmail Account application code: ')
    path_var = ";".join([secret_key, db_username, db_password, db_host, db_port, db_name, gmail_account_address, gmail_account_app_code])
    print(
f"""
You may now add, or update it already exists, the environment variable with the name

{get_project_name()}

and the following value:

{path_var}

... 

After the project has been setup, you can decide to delete this file.
""")


if __name__ == "__main__":
    setup()
