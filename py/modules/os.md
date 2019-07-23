# OS
```python
import os
```

## Environment Variables

```python
os.environ # dict

# All environment variables
print(os.environ)

# Accress to Environment Variable
print(os.environ['HOME'])
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

[_Stack Overflow: Path to parent dir_](https://stackoverflow.com/questions/2860153/how-do-i-get-the-parent-directory-in-python#2860193)
```python
os.path.abspath(os.path.join(yourpath, os.pardir))
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

#### Get list of files

```python
os.listdir(mydir)
```

#### Check file exist

[_Stack Overflow: File exist_](https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions)

```python
os.path.isfile(<path>) 
```

#### Delete file

[_Stack Overflow: Delete files_](https://stackoverflow.com/questions/1995373/deleting-all-files-in-a-directory-with-python)

```python
os.remove(<path>) # file
os.rmdir() # removes an empty directory.
shutil.rmtree() # deletes a directory and all its contents.
```

#### Delete all files

```python
@staticmethod
def clear_dir(path: str):
    """
    Method to clear all files in the dir
    """

    assert os.path.isdir(path)
    files = os.listdir(path)
    for f in files:
        os.remove(f)
```

***

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