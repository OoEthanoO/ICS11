# 1. 
count1 = 1
total1 = 0
while count1 < 11:
    total1 += count1
    count1 += 1
print(total1)

# 2. 
count2 = 100
total2 = 0
while count2 < 201:
    total2 += count2
    count2 += 1
print(total2)

# 3. 
count3 = 200
total3 = 0
while count3 < 301:
    total3 += count3
    count3 += 1
print(total3 - total2)

# 4. 
count4 = 1000
total4 = 0
while count4 < 10001:
    total4 += count4
    count4 += 5
print(total4)

# 5. 
count5 = 1
total5 = 0
while count5 < 101:
    if count5 % 3 != 0:
        total5 += count5
    count5 += 5
print(total5)