def main():
    print(f"Offset for month 1: {month_offset(1)}")
    print(f"Offset for month 2: {month_offset(2)}")
    print(f"Offset for month 3: {month_offset(3)}")
    print(f"Offset for month 4: {month_offset(4)}")
    print(f"Offset for month 5: {month_offset(5)}")
    print(f"Offset for month 6: {month_offset(6)}")
    print(f"Offset for month 7: {month_offset(7)}")
    print(f"Offset for month 8: {month_offset(8)}")
    print(f"Offset for month 9: {month_offset(9)}")
    print(f"Offset for month 10: {month_offset(10)}")
    print(f"Offset for month 11: {month_offset(11)}")
    print(f"Offset for month 12: {month_offset(12)}")
    print(f"Offset for month 43: {month_offset(43)}")


def month_offset(month: int) -> int:
    result = -1
    if month in [1, 10]:
        result = 1
    elif month in [2, 3, 11]:
        result = 4
    elif month in [4, 7]:
        result = 0
    elif month == 5:
        result = 2
    elif month == 6:
        result = 5
    elif month == 8:
        result = 3
    elif month in [9, 12]:
        result = 6
    
    return result


if __name__ == "__main__":
    main()
