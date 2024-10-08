# 1
count1 = 0
while count1 < 11:
    if count1 == 7:
        count1 += 1
        continue
    print(count1)
    count1 += 1
print()

# 2
count2 = 5
total2 = 0
while count2 < 21:
    if count2 % 3 == 0:
        count2 += 1
        continue
    total2 += count2
    count2 += 1
print(total2)
print()

# 3
start3 = int(input("Start: "))
end3 = int(input("End: "))
total3 = 0
while start3 <= end3:
    if start3 == 13 or start3 == 31:
        break
    total3 += start3
    start3 += 1
print(total3)
print()

# 4
while True:
    word = input("Enter a word: ")
    if word == "stop":
        break
    print(f"Your word: {word}")
print("Goodbye!")