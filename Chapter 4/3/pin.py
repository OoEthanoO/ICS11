PIN = "12345"

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")


print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

# 1. A while loop is similar to an if statement in that they both require a condition in order for some code to be
# executed
# 2. A while loop is different from an if statement in that the code in the while loop will keep executing until the
# becomes false while the if statement will only execute the code once if the condition is true
# 3. If PIN was stored as an integer, we will have to cast the entry into a integer before comparing it with the PIN
# 4. If I comment out the input in the while loop, the program will be stuck in an infinite loop after entering the first
# guess. This is because the entry variable is not being updated in the loop and if the condition becomes true it will
# stay true. 