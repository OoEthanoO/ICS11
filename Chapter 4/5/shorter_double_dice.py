import random

print("HERE COMES THE DICE!")
print()

while True:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    sum = roll1 + roll2
    print(f"Roll #1: {roll1}")
    print(f"Roll #2: {roll2}")
    print(f"The total is {sum}!")
    print()

    if roll1 == roll2:
        break