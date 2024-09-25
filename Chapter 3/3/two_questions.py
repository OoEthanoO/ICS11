print("TWO QUESTIONS!")
print("Think of an object, and I'll try to guess it.")
print()

print("Question 1) Is it animal, vegetable, or mineral?")
answer_1 = input("> ")
print()

print("Question 2) Is it bigger than a breadbox?")
answer_2 = input("> ")
print()

guess = ""
if answer_2 == 'yes':
    if answer_1 == 'animal':
        guess = 'moose'
    elif answer_1 == 'vegetable':
        guess = 'watermelon'
    else:
        guess = 'Camaro'
else:
    if answer_1 == 'animal':
        guess = 'squirrel'
    elif answer_1 == 'vegetable':
        guess = 'carrot'
    else:
        guess = 'paper clip'

print(f"My guess is that you are thinking of a {guess}")