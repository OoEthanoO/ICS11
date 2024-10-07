import random

player_health = 100
player_strength = 15
player_potion = 5
base_damage = 5
enemy_health = 100
enemy_strength = 8
enemy_potion = 5

while player_health > 0 and enemy_health > 0:
    print("Both are alive")

    print("1. Attack")
    print("2. Strong Attack")
    print("3. Use potion")
    choice = input("Choose: ")
    if choice == "1":
        print("You chose Attack")
        enemy_health -= base_damage * player_strength
    elif choice == "2":
        print("You chose Strong Attack")
    elif choice == "3":
        print("You chose Use potion")
        if player_potion > 0:
            player_potion -= 1
            player_health += 50
    else:
        print("Invalid option")

    enemy_choice = random.randint(1, 4)
    if enemy_choice == 1:
        print("Enemy chose Attack")
        player_health -= base_damage * enemy_strength
    elif enemy_choice == 2:
        print("Enemy chose Strong Attack")
    elif enemy_choice == 3:
        print("Enemy chose Use potion")
        if (enemy_potion > 0):
            enemy_potion -= 1
            enemy_health += 50

    print("-" * 15)
    print("Player:", player_health)
    print("Enemy:", enemy_health)