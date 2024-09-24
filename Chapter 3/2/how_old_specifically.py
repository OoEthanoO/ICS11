name = input("Hey, what's your name? (Sorry, I keep forgetting): ")
age = int(input(f"Ok, {name}, how old are you? "))

print()
if age < 16:
    print(f"You can't drive, {name}.")
elif age < 18:
    print(f"You can drive but not vote, {name}.")
elif age < 21:
    print(f"You can vote but not rent a car, {name}.")
else:
    print(f"You can do pretty much anything, {name}.")