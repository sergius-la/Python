# Functions

Local functions
```python
def sum_plus_one(a, b):
    def plus_one(x):
        return x + 1
    return plus_one(a + b)
```