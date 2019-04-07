
"""
Python docs dict - https://docs.python.org/3/library/stdtypes.html#dict
"""

# dic = {key, value}
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

