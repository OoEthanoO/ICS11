import math

print("Enter three integers: ")
side1 = int(input("Side 1: "))

side2 = 0
while True:
    side2 = int(input("Side 2: "))
    if side2 >= side1:
        break
    print(f"{side2} is smaller than {side1}.  Try again.")

side3 = 0
while True:
    side3 = int(input("Side 3: "))
    if side3 >= side2:
        break
    print(f"{side3} is smaller than {side2}.  Try again.")
print()

print(f"Your three sides are {side1} {side2} {side3}")
if math.sqrt(side1 ** 2 + side2 ** 2) == side3:
    print("These sides *do* make a right triangle.  Yippy-skippy!")
else:
    print("No!  These sides do not make a right triangle!")