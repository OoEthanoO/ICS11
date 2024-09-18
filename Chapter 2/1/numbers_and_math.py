print("I have a class of 33 students.")
print("There are 11 girls, so that means..")
# prints "there are 22 boys." (33 minus 11 is 22)
print(f"there are {33 - 11} boys.")
print()
# prints "That means 0.3333333333333333 % are girls..." (11 divided by 33 is 0.3 repeated and when rounded to 2
# decimal places it is 0.33)
print(f"That means {round(11 / 33, 2)} % are girls...")
# prints "and 0.6666666666666666 % are boys." (33 minus 11 is 22 and 22 divided 33 is 0.6 repeated and when
# rounded to 2 decimal places it is 0.67)
print(f"and {round((33 - 11) / 33, 2)} are boys.")
print()
print("If we made groups of six...")
# prints "There would be 5 groups of six." (33 divided by 6 is 5.5 and when the decimals are dropped it is 5)
print(f"There would be {33 // 6} groups of six.")
# prints "And then a smaller group of 3 people." (33 divided by 6 gives a remainder of 3)
print(f"And then a smaller group of {33 % 6} people.")
# prints "------------------------------" because it will print '-' 30 times
print("-" * 30)
print("If we had 17 apples and 3 people...")
# prints "Each person would get 5 whole apples." (17 divided by 3 is 5.6 repeated and when the decimals are
# dropped it is 5)
print(f"Each person would get {17 // 3} whole apples.")
# prints "There would be 2 apples remaining." (17 divided by 3 gives a remainder of 2)
print(f"There would be {17 % 3} apples remaining.")
print()
print("If we charged each person $2 each for their 5 apples..")
# prints "they would each pay $10." (2 multiplied by 5 is 10)
print(f"they would each pay ${2 * 5}.")