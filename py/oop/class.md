# Object-oriented programming

## Class

```python
class CamelCaseName:

    @classmethod
    def foo(cls):
        pass

    @staticmethod
    def foo():
        pass

    def __init__(self, attribute: str):
        self._attribute = attribute

    @property
    def attribute(self):
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        self._attribute = attribute
```

## Abstract Class

```python
from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass
```