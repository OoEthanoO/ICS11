stop = int(input("Number: "))
print()

total = 0
for i in range(1, stop + 1):
    print(i, end=" ")
    total += i
print()
print(f"The sum is {total}.")