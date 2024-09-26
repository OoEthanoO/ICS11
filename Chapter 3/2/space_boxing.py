weight = int(input("Please enter your current earth weight: "))
print()

print("I have information for the following planets")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune")
print()

choice = int(input("Which planet are you visiting? "))
print()

multiplier = 0
if choice == 1:
    multiplier = 0.78
elif choice == 2:
    multiplier = 0.39
elif choice == 3:
    multiplier = 2.65
elif choice == 4:
    multiplier = 1.17
elif choice == 5:
    multiplier = 1.05
elif choice == 6:
    multiplier = 1.23

new_weight = weight * multiplier
print(f"Your weight would be {new_weight} pounds on that planet.")