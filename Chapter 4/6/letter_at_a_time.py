message = input("What is your message? ")

print()
print(f"Your message is {len(message)} characters long.")
print(f"The first character is at position 0 and is '{message[0]}'.")
lastpos = len(message) - 1
print(f"The last character is at position {lastpos} and is '{message[lastpos]}'.")
print()
print("Here are all the characters, one at a time:\n")

for i in range(len(message)):
    print(f"\t{i} - '{message[i]}'")

vowel_count = 0
for i in range(len(message)):
    letter = message[i].lower()
    if letter in "aeiouAEIOU":
        vowel_count += 1

print(f"\nYour message contains {vowel_count} vowels.")

# 1
print(range(7)) # prints "range(0, 7)"
print(list(range(7))) # prints "[0, 1, 2, 3, 4, 5, 6]"

# 2. If the message was "Hello", the number 5 would be sent. The numbers that will be included in this range are 0, 1, 2, 3, and 4. The number 5 will not be included in the range.
# 3. If the string variable contains the value "box", its length would be 3. The index of the character 'x' would be 2. 
