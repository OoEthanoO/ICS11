PIN = "12345"
tries = 0
maximum_tries = 4

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < maximum_tries:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= maximum_tries:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")