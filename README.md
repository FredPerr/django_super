# Django Super
## Table of content
1. [Getting Started](#getting-started)
2. [The accounts app](#the-accounts-app)
3. [Template tags](#template-tags)
4. [License](#license)
## Getting started
### Renaming the project
If you wish to rename to project, use the following command:
> python rename-project.py [project-name]

This will rename the entire project except for the root project folder, which you should rename by hand afterwards.
### Starting with a new git repository
If you want to create a project detached from the `django_super` repository, you may delete the `.git` folder at the root of the project folder. You can create a new one afterwards with `git init`.
### Installing the requirements
You may create a new virtual environment with and install the requirements.txt modules with pip. 
> python -m venv venv

__Don't forget to activate the environment before installing the requirements__
> pip install -r requirements.txt


### Adding the environment variables
This project uses environment variables to secure the `SECRET_KEY` and the email account informations such as `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` which are required for the accounts app.

You may add those variables:
[How to add system environment variables on Windows](https://superuser.com/a/949577)
[How to add system environment variables on Max/Unix](https://apple.stackexchange.com/a/106823)

### TypeScript
TypeScript is enabled by default but it is not installed.
To install `tsc`, use `npm` or refer to the [Official TypeScript website](https://www.typescriptlang.org/download)

If you don't want to use TypeScript, you can disable it in the `settings.py` file of the project by setting `USE_TYPESCRIPT` to `False`.

### SASS/SCSS
SASS/SCSS is enabled by default. If you don't want to use it, you can disable it in the `settings.py` file of the project by setting `USE_SCSS` to `False`.

### Others

Django uses SQLite as its database for development.
The `TIME_ZONE` parameter is not configured by default. You may see a list [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List).
`DEFAULT_FROM_EMAIL` parameter in `settings.py` should also be changed.

## The accounts app
By default, the `accounts` app is installed. It provides a custom user model `Account`. An authentication system is configured with that model, which allows for login with email or username.
Views for authentications, password change, password recovery via email and a details view are also setup.

If you don't want to use this app, you can remove it from the `INSTALLED_APPS` in `settings.py` and delete the `accounts` folders. You should also change the `LOGIN_URL` in `settings.py` to another url route along with the `AUTH_USER_MODEL` and `AUTHENTICATION_BACKENDS` settings.

To use the full potential of the app including the password reset system, you must setup a Google Account with an application password:

Go to your `Google Account settings > Security > Enable 2 Steps Verification`
Then, go into `Google Account settings > Security > Application passwords`.
Create a new password and save the key.
You may now add both system environment variables:
`DJANGO_GMAIL_APP_EMAIL` to the gmail address of the account and
`DJANGO_GMAIL_APP_PASSWORD` to the saved key generated for the app.

## Template tags

The template tag `range` simluate the `range()` function in Python. 
Examples:
___
> `10|range`

Outputs
> [0,1,2,3,4,5,6,7,8,9]


With the first argument `zero_index` set to `False`
> `5|range:False`

Outputs
> [1,2,3,4,5]

___

## License
This project uses **Apache License v2**: 
**Permissions**:

#### Commercial use: ####
&#9989; Distribution
&#9989; Modification
&#9989; Patent use
&#9989; Private use

#### Conditions: ####
&#10071; License and copyright notice
&#10071; State changes

#### Limitations: ####
&#10060; Liability
&#10060; Trademark use
&#10060; Warranty

___