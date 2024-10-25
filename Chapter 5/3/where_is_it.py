import random

my_list = []

print("List:", end=" ")
for i in range(10):
    my_list.append(random.randrange(1, 51))
    print(my_list[i], end=" ")
print()

target = int(input("Value to find: "))
print()

found = False
for i, number in enumerate(my_list):
    if number == target:
        found = True
        print(f"{target} is at index {i}.")

if not found:
    print(f"{target} is not in the list.")