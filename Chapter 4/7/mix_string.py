a = input()
b = input()
mixed = ""

for i in range(max(len(a), len(b))):
    if i < len(a):
        mixed += a[i]
    if i < len(b):
        mixed += b[i]

print(mixed)