import random

my_list = []
for i in range(1000):
    my_list.append(random.randrange(10, 100))

for i in range(len(my_list)):
    print(my_list[i], end=" ")