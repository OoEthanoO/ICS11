print("Type in a message, and I'll display it five times.")

message = input("Message: ")

for n in range(2, 21, 2):
    print(f"{n}. {message}")

# 1. Nothing happens when I change n to some other name. You chose to name it n because it is common
# to use a single letter for the variable name in a for loop. 
# 2. The first two arguments (0, 5) change the range of n. 
# 3. The third argument (1) changes the increment or decrement of n. 
# 4. When I call the range function with only one number, that one number becomes the stop value and the
# start value defaults to 0 while the step value defaults to 1. 
# 5. When I call the range function with two numbers, the first number becomes the start value and the second
# number becomes the stop value while the step value defaults to 1.