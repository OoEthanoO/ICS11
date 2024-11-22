def main():
    item_price = -2.99
    quantity = -3
    print(f"{quantity} items at ${item_price} each is:")
    print(f"${calc_subtotal(item_price, quantity)}")


def calc_subtotal(price: float, quantity: int) -> float:
    """Calculate the subtotal for a single item in a cart.
    
    Args:
        price: The price of a single item.
        quantity: Number of a particular item in the cart.

    Returns:
        The subtotal
    """
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    if price < 0:
        raise ValueError("Price cannot be negative.")

    return price * quantity


if __name__ == "__main__":
    main()

# 1. The error is a ValueError with the message "Price cannot be negative." It occurs on line 19 caused by the program
# raising a ValueError when the price is negative. 
# 3. I only see the error message "Quantity cannot be negative" and not "Price cannot be negative."