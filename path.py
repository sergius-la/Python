"""
Paths:
"""

import os.path

# Check existing path
# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
os.path.exists(path)

# Path to file directory
file_dir = os.path.abspath(os.path.dirname(__file__))