# Functions

Local functions
```python
def sum_plus_one(argument: int, b) -> int:
    def plus_one(x):
        return x + 1
    return plus_one(argument + b)
```