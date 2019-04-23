# <img src="/img/py_icon.jpg" width="24" height="24"> Python

<!-- External: -->
<!-- [_Py docs: _]() -->
<!-- [_Stack Overflow: _]() -->
<!-- [_pip docs_]() -->
<!-- Internal: -->
<!-- [__ __]() -->

```python
import this
```

```python 
print("Hello World!")
```

- [_Python 3 docs_](https://docs.python.org/3/)
- [_The Hitchhiker’s Guide to Python!_](https://docs.python-guide.org/)

***

## Variables
- [__variables:__ global, static](/py/var.md)

***

## Functions

- [__functions__](/py/func/func.md)
- [__lambda__](/py/func/lambda.md)
- [__arguments:__ *args, **kwargs](/py/func/args.md)
    - [_[RU] Что означает *args, **kwargs_](https://youtu.be/VJJ9wwzgJCA)
- [__decorators__](/py/func/decorators.md)
    - [_[RU] Декораторы_](https://www.youtube.com/watch?v=Ss1M32pp5Ew)
- [__generators__](/py/func/generaators.md)
- [__Measure execution time__](/py/func/exe_time.md)

## Built-in Functions

- [_Py docs: Built-in Functions_](https://docs.python.org/3/library/functions.html)
    - [__exec()__](/py/built_in_func/py_exec.py)
    - [__help()__](/py/built_in_func/py_help.md)
    - [__enumerate()__]
    - [__sorted()__]
    - [__slice[:]__]
    - [__type()__]
    - [__isinstance()__]

## Try Except (Catch)

- [_Py docs: Try Exept_](https://docs.python.org/3/tutorial/errors.html) 

***

## Data Types

- [__int__]
- [__float__]

## Data Structure

- [_Py docs: String_](https://docs.python.org/3.7/library/string.html)
    - [__string__](/py/data_structure/str.md)
- [_Py docs: Dictinary_](https://docs.python.org/3/library/stdtypes.html#dict)
    - [__dict__](/py/data_structure/dict.md)
- [_Py docs: List_](https://docs.python.org/3/library/stdtypes.html?highlight=list#lists)
    - [__List / Tuple__](/py/data_structure/list.md)
- [_Py docs: Set, Frozenset_](https://docs.python.org/3/library/stdtypes.html?highlight=list#set-types-set-frozenset)
    - [__set__](/py/data_structure/set.md)
- [_Py docs: ENUM_](https://docs.python.org/3/library/enum.html)
    - [__enum__](/py/data_structure/enum.md)
- Collections:
    - [__Counter__](/py/data_structure/counter.md)
    - [__defaultdict__]
    - [__namedtuple__]
    - [__queue__]

***

## OOP

- [__class__](/py/oop/class.md)
- [__Magic methods__](/py/oop/magic_methods.md)
    - [_A Guide to Python's Magic Methods_](https://rszalski.github.io/magicmethods/)

***

## Standard Library

- [__operators__](/py/operators.md)

[_Py docs: The Python Standard Library_](https://docs.python.org/3/library/)

- [_Py docs: Configuration file parser_](https://docs.python.org/3/library/configparser.html)
    - [__config__](/py/config.md)
- [_Py docs: Operating system interfaces_](https://docs.python.org/3/library/os.html)
    - [__os__: Environment Variables, Path](/py/modules/os.md)
    - [__sys__](/py/modules/sys.md)
- [_Py docs: Basic date and time types_](https://docs.python.org/3/library/datetime.html)
    - [_[EN] Date/time value manipulation_](https://pymotw.com/2/datetime/)
    - [_Date time tutorial_](https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/)
- [_Py docs: Virtual Environments and Packages_](https://docs.python.org/3/tutorial/venv.html)
    - [__virtualenv / pip__](/py/pack_venv/vevn_pip.md)
    - [__Modules & Packages__](/py/pack_venv/packahes.md)
    - [__setup.py:__](/py/pack_venv/setup.md)
        - [_Stack overflow: module import error_](https://stackoverflow.com/questions/15368054/import-error-on-installed-package-using-setup-py)
        - [_setup.py (for humans)_](https://github.com/kennethreitz/setup.py)
    - [_Py docs: Installing packages using pip and virtualenv_](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) 
    - [_[RU] Зачем и как использовать virtualenv_](https://youtu.be/wTh-D8GTjeA)
    - [_[RU] Что вам нужно знать о pip_](https://youtu.be/INVi_0pNSg8)
- [_Py docs: DB-API 2.0 interface for SQLite databases_](https://docs.python.org/3.7/library/sqlite3.html)
    - [__sqlite3__](/py/db/sqlite3.mds)
- [_Py docs: CSV File Reading and Writing_](https://docs.python.org/3/library/csv.html)
    - [__csv__](/py/csv.md)
    - [_CVS Files Tutorial_](https://www.programiz.com/python-programming/working-csv-files)
- [__math__](/py/modules/math.py)
- [__struct__]
- [__pickle__]
- [__socket__]

***

## Python application structure

- [_Python-application-layouts_](https://realpython.com/python-application-layouts/)

***

# <img src="/img/django_icon.png" width="24" height="24"> Django

`pip install Django`

[_pip docs_](https://pypi.org/project/Django/)

[_[RU] Уроки Django 2.x_](https://www.youtube.com/watch?v=T0Xi8gWDrQ0&list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX)

[__Django__](/django/django.md)

- [_Django docs: Templates_](https://docs.djangoproject.com/en/2.1/ref/templates/language/)
    - [__Django template__](/django/template.md)
- [_Django docs: Static files_](https://docs.djangoproject.com/en/2.1/howto/static-files/)
- [_Django docs: Lookups_](https://docs.djangoproject.com/en/2.1/ref/models/lookups/)
    - [__Object relation mapping__](/django/orm.md)


***

# <img src="/img/plotly_icon.jpg" width="24" height="24"> Plotly

`pip install plotly`

[_pip docs_](https://pypi.org/project/plotly/)

```
.plot:
    - data[trace]
    - layout
        - buttons
```

- [_Plotly docs_](https://plot.ly/python/)
    - [__Plotly Offline__](/plotly/plotly_offline.md)
    - [_Plotly docs: go.Layout - Buttons_](https://plot.ly/python/custom-buttons/)
        - [__Buttoms__](/plotly/buttons.md)
    - [_Plotly docs: go.Bar_](https://plot.ly/python/bar-charts/)
    - [_Plotly docs: go.Scatter_](https://plot.ly/python/line-and-scatter/)
        - [_Plotly docs: go.Scatter(args)_](https://plot.ly/python/reference/#scatter)
    

***

# <img src="/img/pytest_icon.png" width="24" height="24"> PyTest

`pip install pytest`

[_pip docs_](https://pypi.org/project/pytest/)

- [_PyTest docs_](https://docs.pytest.org/en/latest/)

***

# <img src="/img/open_cv_icon.png" width="24" height="24"> Open CV

`pip install opencv-python`

[_pip docs_](https://pypi.org/project/opencv-python/)

- [_Open CV docs_](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
    - [__Image__](/openCV/image.md)

***

# <img src="/img/requests_icon.png" width="24" height="24"> Requests: HTTP for Humans

`pip install requests`

[_pip docs_](https://pypi.org/project/requests/)

- [_Requests: HTTP for Humans docs_](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)

***

# <img src="/img/selenium_icon.jpg" width="24" height="24"> Selenium with Python

`pip install selenium`

[_pip docs_](https://pypi.org/project/selenium/)

- [_Selenium docs_](https://selenium-python.readthedocs.io/)

***

# <img src="/img/sqlalchemy_icon.jpg" width="64" height="30"> SQLAlchemy

`pip install SQLAlchemy`

[_pip docs_](https://pypi.org/project/SQLAlchemy/)

- [_SQLAlchemy docs_](https://www.sqlalchemy.org/)

*** 

# <img src="/img/bs.jpg" width="24" height="24"> Beautiful Soup

`pip install beautifulsoup4` 

- [_Beautiful Soup docs_](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - [__soup__](/soup/soup.md)

***

# <img src="/img/pandas.jpg" width="64" height="30"> Pandas

`pip install pandas`

[_Pip docs_](https://pypi.org/project/pandas/)

- [_Pandas docs_](https://pandas.pydata.org/)

***

# <img src="/img/numpy.jpg" width="24" height="24"> Numpu

`pip install numpy`

[_Pip docs_](https://pypi.org/project/numpy/) 