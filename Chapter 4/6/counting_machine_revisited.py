start = int(input("Count from: "))
stop = int(input("Count to  : "))
step = int(input("Count by  : "))
print()

for i in range(start, stop + 1, step):
    print(i, end=" ")