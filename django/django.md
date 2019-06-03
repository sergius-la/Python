# Django

### Start Django project
```shell
./django-admin startproject <project name>
./python manage.py startapp <app name>
```

### Run server

```shell
./manage.py runserver <port>
```

### Logging

Print to log

```python
import logging

logger = logging.getLogger(__name__)
logger.error("Hello World")
```