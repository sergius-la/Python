### Dictionary

Python dict - https://docs.python.org/3/library/stdtypes.html#dict

```python
month = {
    1: "January",
    2: "February",
    3: "March"
}

# NOTE: Accessing by index
print(month[1]) # January

# NOTE: Accessing to invalid index
print(month[4]) # KeyError: 4
print(month.get(4, "Not a valid key")) # Not a valid key
```