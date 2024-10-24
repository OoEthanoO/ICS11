import random

my_list = []
for i in range(10):
    my_list.append(random.randrange(1, 101))

for i in range(len(my_list)):
    print("Slot", i, "contains a", my_list[i])