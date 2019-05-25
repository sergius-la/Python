# Virtual Enviroment

#### virtualenv

Install __virtualenv__ package global <br>
`sudo pip install virtualenv`

> Create and Activate local virtual enviroment
`virtualenv venv --python=python3.7 && source venv/bin/activate`

Create a vartual enviroment: <br>
- `python3 -m venv venv`
- `virtualenv venv --python=python3.7`

Activate vartual enviroment:
- Linux:
    - `~` `/venv/bin/activate`
- Mac:
    - `. bin/activate`
- Windows: 
    - `~` `venv\\Scripts\\activate.bat`

***

#### pipenv

Install __pipenv__ package global <br>
`pip install pipenv`

# Package management system

## pip

Install pip

| OS | Command |
| --- | --- |
| macOS | `sudo easy_install pip`|

#### pip install

> Install list of requirements packages <br>
`pip install -r requirements.txt`

- Install package <br>
`pip install <package>`
- Install package from git <br>
`pip install git+<repository_link.git>`
    - Install package from git@branch <br>
    `pip install git+<repository_link.git>@<branch_name>`

Install package for specific version of Python <br>
`python<v> -m pip install <package>` <br>
`python3.7 -m pip install python-barcode`

#### pip uninstall

- Delete package <br>
`pip uninstall <packge>`

#### pip freeze

`pip freeze`
`pip freeze > requirements.txt`