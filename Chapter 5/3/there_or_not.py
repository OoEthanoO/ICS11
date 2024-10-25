import random

my_list = []
print("List:", end=" ")
for i in range(10):
    my_list.append(random.randrange(1, 51))
    print(my_list[i], end=" ")
print()

target = int(input("Value to find: "))
found = False

for number in my_list:
    if number == target:
        found = True
        break

if found:
    print(f"{target} is in the list.")
else:
    print(f"{target} is not in the list.")