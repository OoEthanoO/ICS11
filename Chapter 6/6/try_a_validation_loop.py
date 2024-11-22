def main():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print("Need to input an integer!\n")
    print(f"Wow, you are {age} years old.")


if __name__ == "__main__":
    main()

# 1. We get a ValueError when we try to convert a string that is not an integer to an integer.
# 4. The loop doesn't break right after taking the input because we want to keep asksing for the input until we get an integer.