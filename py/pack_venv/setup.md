# setup.py

#### Python package structure

```
package_root/
│
├── package/
│   ├── __init__.py
|   |── __version__.py
│   ├── package.py
│   └── helpers.py
│
├── tests/
│   ├── package_tests.py
│   └── helpers_tests.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```

```python
import os
from setuptools import setup

NAME = "package"
VERSION = None

package_root = os.path.abspath(os.path.dirname(__file__))

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_")
    with open(os.path.join(package_root, project_slug, '__version__.py')) as file:
        exec(file.read(), about)
        VERSION = about["__version__"]

setup (
    name = NAME,
    version =  VERSION,
    package_dir={'': "package"},
    packages=[''],
    install_requires=[
        "normal_package",
        "private_package @ git+<git_link>.git" # pip 18.0.0
    ]
)
```