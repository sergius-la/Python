# Dictinary

 Method | Description |
| --- | --- |
| .items() | |
| .keys() | |
| .values() | |

```python
dict # "assignment
dict() # initialization
```

```python
# dict = {key, value}
months = {
    1: "January",
    2: "February",
    3: "March"
}

# Add new element - O(1)
months[1]="December"

# Update value
# Python docs - https://docs.python.org/3/library/stdtypes.html#dict.update
months[1]="January"

# NOTE: Print dict
print("{" + "\n".join("{}: {}".format(k, v) for k, v in months.items()) + "}")

# Keys
dict.keys() # Get [key, key]
dict.values() # Get [value, value]


# NOTE: Accessing by index - O(1)
print(months[1]) # January

# NOTE: Accessing to invalid index
print(months.get(4, "Not a valid key")) # Not a valid key
print(months[4]) # raise KeyError: 4


"""
NOTE: Loop over dictionaries
https://stackoverflow.com/questions/3294889/iterating-over-dictionaries-using-for-loops
"""

for key, value in months.items():
    print("Key {}".format(key))
    print("Value {}".format(value))

"""
Change the key name
https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
"""

dictionary[new_key] = dictionary.pop(old_key)


"""
Find Max / Min - Value
http://www.aroseartist.com/python-dictionary-max-min/
"""

letter_dict = {'l': 5, 'g': 2, 'b': 1, 't': 3}
max(letter_dict, key = lambda x: letter_dict.get(x))

def __min_key(dict):
    return min(dict.keys(), key=(lambda k: dict[k]))


"""
Updating dict 
"""

d1 = {"a":1, "c":3}
d2 = {"a":2, "b":5}
d1.update(d2)
print(d1) # {'a': 2, 'c': 3, 'b': 5}
```