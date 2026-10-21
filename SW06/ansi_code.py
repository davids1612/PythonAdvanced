from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

x = Color.RED

print(type(Color.RED), type(x))
print(x.name)
print(x.value)
print(type(x.value))
print(type(x.name))

