# django_super
**Utility Scripts, Preinstall SCSS & Base Template for quick startup**

This Django project has `SCSS` preinstalled alongside a quick project _renaming script_ and a base template that handles the `static` folder related common tasks. 

___
## Scripts
`rename.py`: A one-liner renaming script for your Django project.
_Run the script with the following command pattern:_
> `python rename.py (project name)`

___

## Requirements / Dependencies ##
Install the virutal environment:
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
```
Commercial use:
    Distribution
    Modification
    Patent use
    Private use

Conditions:
    License and copyright notice
    State changes

Limitations:
    Liability
    Trademark use
    Warranty
```

___