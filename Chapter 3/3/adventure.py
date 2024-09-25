print("Welcome to my house!")
print()

print("You are at the front door of my house, would like to go inside through the \"main\" door or the \"garage\"?")
choice_1 = input("> ")

if choice_1 == "main":
    print("You are now inside the house. You see a staircase that leads upstairs. Would you like to go upstairs?")
    print("(\"yes\" or \"no\")")
    choice_2 = input("> ")

    if choice_2 == "yes":
        print("There's an emergency. You really want to go to the washroom. You have two choices. Do you want to")
        print("go to the \"washroom\" on the left or go to my \"room\" on ther right?")
        choice_3 = input("> ")
        if choice_3 == "washroom":
            print("You go to the washroom and you see a mirror. You look at yourself and see a ghost behind you.")
            print("You panicked and you tripped on your way down the stairs and died.")
        elif choice_3 == "room":
            print("You die a horrible death from not being able to go to the washroom and holding it in")
    elif choice_2 == "no":
        print("You stay downstairs and you see a door that leads to the basement. Would you like to go to the")
        print("basement? (\"yes\" or \"no\")")
        choice_3 = input("> ")
        if choice_3 == "yes":
            print("You go to the basement and you see a ghost. You scream and run out of the house.")
        elif choice_3 == "no":
            print("You stay in the living room, ate some snacks, and had a great time.")
elif choice_1 == "garage":
    print("You are now inside the garage. As you enter, the garage door slowly closes behind you. You have two")
    print("options. Do you want to \"enter\" the house or quickly \"run out\" of the garage before the door closes?")
    choice_2 = input("> ")
    if choice_2 == "enter":
        print("As you try to open the door that leads in the house, you realize that the door is locked. Do you")
        print("try to \"pick\" the lock or change your mind and \"run\" out of the garage?")
        choice_3 = input("> ")
        if choice_3 == "pick":
            print("You successfully pick the lock. You now enter the house and have a good time")
        elif choice_3 == "run":
            print("You attempt to run out of the garage. Unfortunately, the door closes before you can make it out.")
            print("You suffocate and die.")
    if choice_2 == "run out":
        print("You successfully run out of the garage before the door closes. You are safe. Do you still want to")
        print("enter the house via the front door")
        choice_3 = input("> ")
        if choice_3 == "yes":
            print("You enter the house and have a good time.")
        elif choice_3 == "no":
            print("You leave the house and go home.")