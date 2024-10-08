import random

target = random.randrange(1, 11)
print("I'm thinking of a number from 1 to 10. Try to guess it.")
attempts = 0

while True:
    print("That is incorrect. Guess again.")
    attempts += 1
    guess = int(input("Your guess: "))
    if guess == target:
        break

print("That's right! You're a good guesser.")
print(f"It only took you {attempts} tries.")