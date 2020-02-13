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
        # Attribute check
        if not isinstance(attribute, str):
            raise TypeError("attrib must be str, not %s" % (
                attribute.__class__.__name__,))
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

## [_Stack Overflow: Static Class_](https://stackoverflow.com/questions/30556857/creating-a-static-class-with-no-instances)

```python
class World(object):
  elements = []

  @staticmethod
  def add_element(x):
    World.elements.append(x)
```