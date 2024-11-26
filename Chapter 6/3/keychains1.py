def add_keychain(num_keychains: int) -> int:
    num_to_add = int(input(f"You have {num_keychains} keychains. How many to add? "))
    if num_to_add < 0:
        print("You can't add a negative number of keychains.")
        return num_keychains
    return num_keychains + num_to_add

def remove_keychain(num_keychains: int) -> int:
    num_to_subtract = int(input(f"You have {num_keychains} keychains. How many to remove? "))
    if num_to_subtract < 0:
        print("You can't remove a negative number of keychains.")
        return num_keychains
    
    if num_to_subtract > num_keychains:
        print("You can't remove more keychains than you have.")
        return num_keychains
    return num_keychains - num_to_subtract
    
def view_order(num_keychains: int, price_per_keychain: float, tax: float, base_shipping: int, per_keychain_shipping: int) -> None:
    print(f"You have {num_keychains} keychains.")
    print(f"Keychains cost ${price_per_keychain} each.")
    print(f"Shipping cost is ${base_shipping} plus ${per_keychain_shipping} per keychain.")
    subtotal = num_keychains * (price_per_keychain + per_keychain_shipping) + base_shipping
    print(f"Subtotal: ${subtotal:.2f}.")
    tax_amount = subtotal * tax
    print(f"Tax: ${tax_amount:.2f}.")
    print(f"Total cost is ${subtotal + tax_amount:.2f}.")

def checkout(num_keychains: int, price_per_keychain: float, tax: float, base_shipping: int, per_keychain_shipping: int) -> None:
    print("CHECKOUT")
    print()
    name = input("What is your name? ")
    view_order(num_keychains, price_per_keychain, tax, base_shipping, per_keychain_shipping)
    print(f"Thanks for your order, {name}!")

def main():
    num_keychains = 0
    PRICE_PER_KEYCHAIN = 10
    TAX = 0.13
    BASE_SHIPPING = 5
    PER_KEYCHAIN_SHIPPING = 1

    print("Ye Olde Keychain Shoppe")
    while True:
        print()
        print("1. Add Keychains to Order")
        print("2. Remove Keychains from Order")
        print("3. View Current Order")
        print("4. Checkout")
        print()
        choice = int(input("Please enter your choice: "))
        print()
        if choice == 1:
            num_keychains = add_keychain(num_keychains)
            print(f"You now have {num_keychains} keychains.")
        elif choice == 2:
            num_keychains = remove_keychain(num_keychains)
            print(f"You now have {num_keychains} keychains.")
        elif choice == 3:
            view_order(num_keychains, PRICE_PER_KEYCHAIN, TAX, BASE_SHIPPING, PER_KEYCHAIN_SHIPPING)
        elif choice == 4:
            checkout(num_keychains, PRICE_PER_KEYCHAIN, TAX, BASE_SHIPPING, PER_KEYCHAIN_SHIPPING)
            break

if __name__ == "__main__":
    main()