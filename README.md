# django_super
**Preinstalled _SCSS_ & and _TypeScript_, Utility Script commands and Base Template for a quick Django project startup!**

This Django project has `SCSS` and `TypeScript` preinstalled alongside a quick project _renaming_ and _install_ scripts and a base template that handles the `static` folder related common tasks. 

___
## Script ([supervisor.py](https://github.com/FredPerr/django_super/blob/main/supervisor.py)) ##

`supervisor.py` is the command line manager for the scripts of this application.

The available commands are the following:
- `rename-project`: Rename the Django Project to the given value.
- `select-compilers`: Choose the compilers used in the project (**TypeScript** & **SCSS**).

___

## Requirements / Dependencies ##
- Install the virutal environment:
`pip install -r requirements.txt`

    which includes:
    ```txt
    asgiref==3.3.1
    Django==3.1.7
    django-appconf==1.0.4
    django-compressor==2.4
    django-libsass==0.8
    libsass==0.20.1
    pytz==2021.1
    rcssmin==1.0.6
    rjsmin==1.1.0
    six==1.15.0
    sqlparse==0.4.1
    ```

- TypeScript (tsc) if activated in the project.

    Install TypeScript with `npm` or refer to the [Official TypeScript website](https://www.typescriptlang.org/download)
\
 _By default, TypeScript is activated in the project, if you wish to disable it and not ultimately not install tsc, make sure to run the command `python supervisor.py select-compilers False (True or False for SCSS)`._

___

## Project structure

&#x1F4C1;django_super/ &nbsp;&#8594; Main files of the django project (`settings.py`, `urls.py`, ...).

&#x1F4C1;static/ &nbsp;&#8594; _Scripts_, _Stylesheets_ and _Images_ files.

&#x1F4C1;super/ &nbsp;&#8594; Default main application containing the `super.html` base template and the `home.html` template. `home.html` extends `super.html`. By default `home.html` is the root url rendered page. 

&#x1F4C1;super/templatetags &nbsp;&#8594; Contains useful template tags that may be added in the project such as `range`.


## Template tags ##

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

## License ##

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