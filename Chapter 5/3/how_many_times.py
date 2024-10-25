import random

my_list = []
print("List:", end=" ")
for i in range(10):
    my_list.append(random.randrange(1, 51))
    print(my_list[i], end=" ")
print()

target = int(input("Value to find: "))
count = 0

for number in my_list:
    if number == target:
        count += 1

print(f"{target} was found {count} times.")