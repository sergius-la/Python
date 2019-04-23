"""
Global variables - https://stackoverflow.com/questions/10588317/python-function-global-variables
"""

global someVar
someVar = 55

# Using global variable in function
# https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
res = 1
def add():
    global res
    res += 1

if __name__ == '__main__':

    add()
    print(res)


# Class static variavle
# https://stackoverflow.com/questions/68645/are-static-class-variables-possible

class MyClass:
    i = 3

    @staticmethod
    def static_print():
        print(MyClass.i)