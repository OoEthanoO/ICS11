# 1
animal_names = "monkey bat cat dog"
for name in animal_names.split(" "):
    print(name)

# 2
integers_string = "65, 72, 32, 22"
integers_list = []
for i, integer in enumerate(integers_string.split(", ")):
    integers_list.append(int(integer))
    print(f"{i}: {integer}")

# 3
number_string = "one,two,three,four"
number_list = []
for number in number_string.split(","):
    if number == "zero":
        number_list.append(0)
    elif number == "one":
        number_list.append(1)
    elif number == "two":
        number_list.append(2)
    elif number == "three":
        number_list.append(3)
    elif number == "four":
        number_list.append(4)
    elif number == "five":
        number_list.append(5)
print(number_list)

# 4
win_loss_string = "W W L T T W"
win_loss_list = []
for win_loss in win_loss_string.split(" "):
    if win_loss == "W":
        win_loss_list.append(2)
    elif win_loss == "L":
        win_loss_list.append(0)
    elif win_loss == "T":
        win_loss_list.append(1)
print(win_loss_list)

# 5
x_pos_string = "x:3,x:6,x:14,x:22"
x_pos_list = []
for x_pos in x_pos_string.split(","):
    x_pos_list.append(int(x_pos.split(":")[1]))
print(x_pos_list)

# 6
coordinate_string = "x:2,y:5 - x:5,y:11 - x:7,y:14"