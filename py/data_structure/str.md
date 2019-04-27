# String

methods:
- .lower() - hello world!
- .upper() - HELLO WORLD!
- .split()
- .strip()
- .capitalize()
- .isspace()

```python
"""
Python String Literals - https://docs.python.org/3/reference/lexical_analysis.html#literals
"""

class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

kenwood = Kettle("Kenwood", 14.55)

print("Model: {0.make} = {0.price}".format(kenwood)) # Model: Kenwood = 14.55

a = "BMW"
b = "M5"
print("Model: {} - {}".format(a, b)) # Model: BMW - M5

x = "123"
x = "ABC"
print(x.index("B")) # 1
print(x.index("D")) # ValueError: substring not found

raw_string = r""

new_line = "\n"

tab_string = "1\t2\t3\t4"

splited_string = """First line
second line
third line """



Remove witespaces from a string.
str.strip()
https://stackoverflow.com/questions/251464/how-to-get-a-function-name-as-a-string-in-python

String -> int
x = "5"
y = int(x)

input()
name = input("Enter your name: ")
print("Hello " + name)

Print() - int -> String
num = 5
print(str(num) + " Five")
```

[Stack overflow: String is empty?](https://stackoverflow.com/questions/9573244/most-elegant-way-to-check-if-the-string-is-empty-in-python)