
import math

def Triangle(b,h):
    area = (b * h)/ 2
    return area
def Rectangle(b,h):
    area = (b * h)
    return area
def Square(b):
    area = b **2
    return area
def Circle(b,h):
    area = math.pi * (h/2)
    return area

def menu():
    print("===================")
    print("Area Calculator 📐")
    print("===================")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")

menu()
selected_shape = int(input("Which Shape: "))
while selected_shape != 5:

    b = int(input("Base:" ))
    h = int(input("Height:" ))
    if selected_shape == 1:
        print(Triangle(b,h))
    elif selected_shape == 2:
        print(Rectangle(b,h))
    elif selected_shape == 3:
        print(Square(b))
    elif selected_shape == 4:
        print(Circle(b,h))
    else:
        break
    menu()
    selected_shape = int(input("Which Shape: "))
print("You have quit")
