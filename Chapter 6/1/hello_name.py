# Intro to Functions Practice - Hello, Name!

def main():
    name = input("Enter your name: ")

    if name == "":
        name = "User"

    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()