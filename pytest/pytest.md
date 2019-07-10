# PyTest

## Run tests

- `py.test -v`
    - skip tests details - `py.test -v -rxs`
- `python -m pytest`


## Naming

Tests file starting with `test_`
```
test_<name>.py
```

```python
# content of test_class.py

class TestClass(object):

    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_<name>(self):
        x = "hello"
        assert hasattr(x, 'check')
```

## Tests hierarchy

[_PyTest docs: Group multiple tests in a class_](https://docs.pytest.org/en/latest/getting-started.html#group-multiple-tests-in-a-class)

Skip test

```python
import pytest

@pytest.mark.skip(reason="#")
def test_sum()
    x = 2 + 2
    assert x == 4
```

Skip by conditions

```python
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3,3), reason="#")
def test_sum()
    x = 2 + 2
    assert x == 4
```

## Parametrizing tests / DataProvider

```python
testdata = [
        (2, 2, 2),
        (4, 4, 8)
]

@pytest.mark.parametrize("x, y, expected", testdata)
def test_get_range(x, y, expected):
    assert x + y == expected
```