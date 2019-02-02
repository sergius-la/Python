### List

Python list - https://docs.python.org/3/library/stdtypes.html#list

```python
x = [1, 2, 3, 4, 5]

print(x[-1]) # 5 - Accesing with negative index will grab from back
print(x[1:3]) # [2, 3]

# Copy Lists
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)

pop()
x = [1, 2, 3, 4, 5]
y = x.pop()
print(y) # 5

x = [1, 2, 3, 4, 5, 5]
print(x.count(5)) # 2 
```