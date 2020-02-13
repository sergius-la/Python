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

## Logs

[_Django docs: Logging_](https://docs.djangoproject.com/en/dev/topics/logging/)

```python
import logging

logger = logging.getLogger(__name__)
logger.error("Hello Error")
```

## [Models](/django/models.md)