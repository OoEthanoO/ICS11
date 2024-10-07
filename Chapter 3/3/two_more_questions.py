print("TWO MORE QUESTIONS, BABY!")
print()

print("Think of something and I'll try to guess it!")
print()

choice_1 = input("Does it stay inside or outside or both? ")
choice_2 = input("Is it a living thing? ")
print()

guess = ""
if choice_1 == "inside" and choice_2 == "yes":
    guess = "houseplant"

if choice_1 == "inside" and choice_2 == "no":
    guess = "shower curtain"

if choice_1 == "outside" and choice_2 == "yes":
    guess = "bison"

if choice_1 == "outside" and choice_2 == "no":
    guess = "billboard"

if choice_1 == "both" and choice_2 == "yes":
    guess = "dog"

if choice_1 == "both" and choice_2 == "no":
    guess = "cell phone"

print(f"Then what else could you be thinking of besides a {guess}?!?")