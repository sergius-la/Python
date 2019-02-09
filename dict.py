
"""
Python docs dict - https://docs.python.org/3/library/stdtypes.html#dict
"""

months = {
    1: "January",
    2: "February",
    3: "March"
}

"""
NOTE: Update value
Python docs - https://docs.python.org/3/library/stdtypes.html#dict.update
"""
months[1]="December"

# NOTE: Print dict
print("{" + "\n".join("{}: {}".format(k, v) for k, v in months.items()) + "}")

# NOTE: Accessing by index
print(months[1]) # December

# NOTE: Accessing to invalid index
print(months.get(4, "Not a valid key")) # Not a valid key
print(months[4]) # raise KeyError: 4


