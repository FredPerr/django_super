# Django Super

## Table of content

1.  [Project features](#features)
2.  [Setup](#setup)
3.  [License](#license)

## Features

  - Custom __email__ based User model
  - __Password Recovery__ & __User Management__ views
  - Preconfigured __Dart SCSS__ implementation
  - Implemented __FontAwesomeFree__
  - __PostgreSQL__ 2 Database configuration
  - Secured Configuration (Credentials and Keys)
  - __Email System__



## Setup
1. Define and activate a virtual environment with `python -m venv venv` and run `./venv/Scripts/activate` (for Unix based OS) or `./venv/Scripts/Activate.ps1` for PowerShell
2. Init a new git if needed (`git init`)
3. Install the _pip_ requirements with `pip install -r requirements.txt`
4. Install [Dart SASS](https://github.com/sass/dart-sass#readme) on your computer
5. Create a PostgreSQL database for the project
6. *[Recommended]* Install pgAdmin for PostgreSQL management
7. __Create__ or __Use__ a [Google account with __2 step verification__](https://myaccount.google.com/intro/security) and create an application password (__keep that password__). The path is `Google Account settings > Security > Enable 2 Steps Verification`, enable it. Then, `Google Account settings > Security > Application passwords` and create a new app password (your may choose a custom name such as the name of your application).
8. Configure your project with `python setup.py` and follow the instructions.
9. Refresh your system environment variables by restarting your computer or using a command.
10.  Create the superuser with `python manage.py createsuperuser`
11. Apply migrations with `python manage.py makemigrations` and `python manage.py migrate`


If your are finished with the configuration, you can delete the setup.py file.


### Setup Validation
Run the server with `python manage runserver`
Go to `localhost:8000` and verify the checklist (with the email system)
  
Dart SASS and FontAwesome are not dependent on each other. If one fails, please read the instruction on their respective website to install.

For the Email system, changes may happen such as the recent removal of _less secure apps_ system. Please open a ticket if that is the case.

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