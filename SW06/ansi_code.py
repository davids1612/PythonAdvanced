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


color1 = Color.RED
color2 = Color.BLUE

if color1 == Color.RED:
    print("color1 is red.")

if color1 is Color.RED:
    print("color1 is Color.RED")

print(color1 == 1)
print(color1.value == 1)