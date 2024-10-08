import random


# again = "y"

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")

    if again != "y":
        break

# 3. The loop still works after deleting the line "again = "y"" because t he again variable is created in the
# loop and nothing outside of the loop needs to use that variable. 