import random

target = random.randrange(1, 11)
print("I'm thinking of a number from 1 to 10.")
guess = int(input("Your guess: "))
print()

if guess == target:
    print(f"That's right! My secret number was {target}!")
else:
    print(f"Sorry, but I was really thinking of {target}.")