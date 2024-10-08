import random

target = random.randint(1, 100)
print("I'm thinking of a number from 1-100. You have 7 guesses.")
guess = int(input("First guess: "))
attempts = 1

while attempts < 7 and guess != target:
    if guess < target:
        print("Sorry, you are too low.")
    else:
        print("Sorry, that guess is too high.")
    guess = int(input(f"Guess # {attempts + 1}: "))
    attempts += 1

if guess == target:
    print("You guess it! What are the odds?!?")
else:
    print(f"Sorry, you didn't guess it in 7 tries. You lose.")