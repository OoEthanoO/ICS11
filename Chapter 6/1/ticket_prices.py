# Intro to Functions Practice - Ticket Prices

TICKET_PRICE = 13.95

def main():
    ticket_count = int(input("How many tickets? "))
    print(f"Total cost would be {ticket_count * TICKET_PRICE}")

if __name__ == "__main__":
    main()