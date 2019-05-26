# OS
```python
import os
```

## Environment Variables

Print environment variables
```python
print(os.environ)
```

[_Stack Overflow: Set / Edit environment variables_](https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python)
```python
os.environ["DEBUSSY"] = "1"
```

## Path

Methods:
- os.path.exists()
- os.path.isfile()

[_Stack Overflow: Check existing path_](https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions)
```python
import os.path

os.path.exists("<path>")
```

Path to the file's directory
```python
file_dir = os.path.abspath(os.path.dirname(__file__))
```

Check path to a file
```python
os.path.isfile("<path>")
```

[_Stack Overflow: Set / List of files and dirs_](https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory)

[_Py docs: os.listdir_](https://docs.python.org/2/library/os.html#os.listdir)

```python
files = os.listdir("path")
```

Save dirs names into csv file

```python
def save_dirs(path: str):
    dirs = os.listdir(path)
    with open("paths.csv", 'w',  newline='') as csvFile:
        writer = csv.writer(csvFile)
        for row in dirs:
            writer.writerow([row])
        csvFile.close()
```

## Dirs

[_Stack Overflow: Safety create dirs exist_](https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory)

```python
import os
if not os.path.exists(directory):
    os.makedirs(directory)
```

## Files

#### Check file exist

[_Stack Overflow: File exist_](https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions)

```python
import os.path
os.path.isfile(<path>) 
```

## Process id

```puthon
os.getpid()
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