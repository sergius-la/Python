# OS
```python
import os
```

## Environment Variables

Print environment variables
```python
print(os.environ)
```

 Set / Edit environment variables - [Stack Overflow](https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python)
```python
os.environ["DEBUSSY"] = "1"
```

## Path

[_Stack Overflow: Check existing path_](https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions)
```python
import os.path

os.path.exists("<path>")
```

Path to the file's directory
```python
file_dir = os.path.abspath(os.path.dirname(__file__))
```

<!-- """
TODO: Command In, Read command output
read from concole os.popen().read()

# TODO:
Creating Directory - https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
""" -->

<!-- 

"""
List of files and dirs:
https://docs.python.org/2/library/os.html#os.listdir
https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
"""
files = os.listdir("path")


"""
https://docs.python.org/3/library/os.html#os.walk
"""
os.walk()

"""
Path
""" -->