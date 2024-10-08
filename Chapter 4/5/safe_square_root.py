import math

print("SQUARE ROOT!")
num = int(input("Enter a number: "))
while num < 0:
    print("You can't take the square root of a negative number, silly.")
    num = int(input("Try again: "))

root = math.sqrt(num)
print(f"The square root of {num} is {root}.")