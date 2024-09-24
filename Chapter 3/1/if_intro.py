robot_location = 34
ball_location = 40
goal_location = 10
have_ball = False

if robot_location < ball_location:
    # prints "Almost at the ball" if robot_location is less than ball_location
    print("Almost at the ball") 

if robot_location > goal_location:
    # prints "You are beyond the goal." if robot_location is greater than goal_location
    print("You are beyond the goal.")

if robot_location == goal_location:
    # prints "The robot is at the goal." if robot_location is equal to goal_location
    print("The robot is at the goal.")

robot_location += 6 # add 6 to robot_location

if robot_location == goal_location:
    # prints "At the goal." if robot_location is equal to goal_location
    print("At the goal.")

if robot_location == ball_location:
    # prints a few messages and pick up the ball if robot_location is equal to ball_location
    print("At the ball")
    print("Picking up the ball.")
    have_ball = True
    print("Now make your way to the goal.")

robot_location -= 30 # subtract 30 from robot_location

if robot_location < goal_location:
    # prints "You went too far." if robot_location is less than goal_location
    print("You went too far.")

if robot_location == goal_location and have_ball is True:
    # prints "You scored a goal!" if robot_location is equal to goal_location and have_ball is True
    print("You scored a goal!")
    have_ball = False

# The purpose of indenting in the if statement is to show what code is a part of the if statement and what code is
# not
# If a code is indented, it is a part of the if statement, and if it is not, it is not a part of the if statement