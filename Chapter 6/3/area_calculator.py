import math

def area_circle(radius: int) -> float:
    return math.pi * radius ** 2

def area_rectangle(length: float, width: float) -> float:
    return length * width

def area_square(side: float) -> float:
    return side ** 2

def area_triangle(base: float, height: float) -> float:
    return base * height / 2

print("Shape Area Calculator version 0.1 (c) 2024 Ethan, Inc.")

while True:
    print()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print()
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")
    option = int(input("Which shape: "))
    print()

    if option == 1:
        base = float(input("Base: "))
        height = float(input("Height: "))
        print()
        area = area_triangle(base, height)
        print(f"The area is {area}")
    elif option == 2:
        length = float(input("Length: "))
        width = float(input("Width: "))
        print()
        area = area_rectangle(length, width)
        print(f"The area is {area}")
    elif option == 3:
        side = float(input("Side: "))
        print()
        area = area_square(side)
        print(f"The area is {area}")
    elif option == 4:
        radius = int(input("Radius: "))
        print()
        area = area_circle(radius)
        print(f"The area is {area}")
    elif option == 5:
        print("Goodbye.")
        break