import random

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 101))

my_second_list = []
for i in range(len(my_list)):
    my_second_list.append(my_list[i])

my_list[-1] = -7

print("List 1:", end=" ")
for i in range(len(my_list)):
    print(my_list[i], end=" ")
print()

print("List 2:", end=" ")
for i in range(len(my_second_list)):
    print(my_second_list[i], end=" ")