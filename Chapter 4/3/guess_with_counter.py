import random

target = random.randrange(1, 11)
print("I'm thinking of a number from 1 to 10. Try to guess it.")
guess = int(input("Your guess: "))
attempts = 1

while guess != target:
    print("That is incorrect. Guess again.")
    attempts += 1
    guess = int(input("Your guess: "))

print("That's right! You're a good guesser.")
print(f"It only took you {attempts} tries.")