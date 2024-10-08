import random

target = random.randrange(1, 11)
print("I'm thinking of a number from 1 to 10. Try to guess it.")
guess = int(input("Your guess: "))

while guess != target:
    print("That is incorrect. Guess again.")
    guess = int(input("Your guess: "))

print("That's right! You're a good guesser.")