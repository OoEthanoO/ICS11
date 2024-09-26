ready = input("Are you ready or a quiz? ")
print()
if ready == "Y":
    correct_count = 0
    print("Q1) What is the capital of Alaska?")
    print(" " * 8 + "1) Melbourne")
    print(" " * 8 + "2) Anchorage")
    print(" " * 8 + "3) Juneau")
    print()

    choice = int(input("> "))
    print()
    if choice == 3:
        print("That's right!")
        correct_count += 1
    else:
        print("Sorry, the correct answer is 3) Juneau.")
    print()

    print("Q2) In Python, the way you get keyboard input is the keyboard_input function.")
    print(" " * 8 + "1) true")
    print(" " * 8 + "2) false")
    print()

    choice = int(input("> "))
    print()
    if choice == 2:
        print("That's right!")
        correct_count += 1
    else:
        print("Sorry, in Python, you would use the \"input\" function to get keyboard input.")
    print()

    print("Q3) What is the result of 9 + 6 / 3?")
    print(" " * 8 + "1) 5")
    print(" " * 8 + "2) 11")
    print(" " * 8 + "3) 15/3")
    print()

    choice = int(input("> "))
    print()
    if choice == 2:
        print("That's correct!")
        correct_count += 1
    else:
        print("Sorry, the correct answer is 2) 11.")
    print()
    print()

    print(f"Overall, you got {correct_count} out of 3 correct.")
    print("Thanks for playing!")
else:
    print("Goodbye!")