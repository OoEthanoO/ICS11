print("Type in a message, and I'll display it several times.")

message = input("Message: ")
print()

times = int(input("How many times? "))
n = 0
while n < times * 10:
    print(f"{n + 10}. {message}")
    n += 10
    # n += 1 prevents the loop from running indefinitely by incrementing n by 1 each time the loop runs.