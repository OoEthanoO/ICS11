import random

print("HERE COMES THE DICE!")
print()

roll1 = 0
roll2 = 1

while roll1 != roll2:
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    sum = roll1 + roll2
    print(f"Roll #1: {roll1}")
    print(f"Roll #2: {roll2}")
    print(f"The total is {sum}!")
    print()