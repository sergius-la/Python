# Function arguments

```python
## No-named args, Named args

## *args - tuple
## **kwargs - dict

def add(*args):
    print()
    print(args)
    # print("sum {}".format(sum(args)))
    # print("len {}".format(len(args)))
    print()

add(1, 2, 3)

l = [1, 2, 3]
add(*l)

# Named Args, # Default Args
def say(who, name=None):
    print("{} {}".format(who, name))

# Check defaults Arguments
print(say.__defaults__)
```