in1 = input()

for i in range(len(in1) - 2):
    if in1[i] == "b" and in1[i + 2] == "b":
        print(True)
        exit()

print(False)