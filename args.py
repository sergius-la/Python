"""
[RU] Что означает *args, **kwargs - https://youtu.be/VJJ9wwzgJCA
"""

def add(*args):
    print()
    print(args)
    # print("sum {}".format(sum(args)))
    # print("len {}".format(len(args)))
    print()

add(1, 2, 3)

l = [1, 2, 3]
add(*l)