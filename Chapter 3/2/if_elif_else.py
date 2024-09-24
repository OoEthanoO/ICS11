team_a_points = 25
team_a_wins = 15

team_b_points = 20
team_b_wins = 16

if team_a_points > team_b_points:
    print("Team A wins!")
    team_a_wins += 1
if team_b_points > team_a_points:
    print("Team B wins!")
    team_b_wins += 1
else:
    print("Tie.")

if team_a_wins > team_b_wins:
    print("Team A has more wins than Team B.")
elif team_b_wins > team_a_wins:
    print("Team B has more wins than Team A.")
else:
    print("Both Teams A and B have the same number of wins.")

# Even though team_a_wins is initialized as 15 and team_b_wins is initialized as 16, the first if statement will
# add one to the team with a higher number of points. In this case, team_a_points is 25 and team_b_points is 20,
# so team_a_wins will be incremented by 1. Now, team_a_wins is 16 and is equal to team_b_wins, so the else statement
# now gets executed and prints "Both Teams A and B have the same number of wins."

# "elif" is used to add another condition to an existing if statement that gets executed if all the previous
# conditions are false and its own condition is true. "else" is used to execute a block of code if all the previous
# conditions are false. 

# if I change an "elif" to just "if", now the previously "elif" statement could be executed even if the previous
# if statement is true. 