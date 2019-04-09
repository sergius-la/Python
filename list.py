
"""
Python list - https://docs.python.org/3/library/stdtypes.html#list
Python tuple - TODO: Add link
"""

x_list = list()
x = [1, 2, 3, 4, 5]

print(x[-1]) # 5 - Accesing with negative index will grab from back
print(x[1:3]) # [2, 3]

# Append a new element - O(1)
x.append(6)

# Insert a new element - O(n)
x.insert(0, 0)

# Copy Lists
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)

x = [1, 2, 3, 4, 5]
y = x.pop()
print(y) # 5

x = [1, 2, 3, 4, 5, 5]
print(x.count(5)) # 2 