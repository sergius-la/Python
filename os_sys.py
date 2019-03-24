"""
TODO: Command In, Read command output
read from concole os.popen().read()

# TODO:
Creating Directory - https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory-in-python
"""

import os

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