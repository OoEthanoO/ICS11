

def main():
    print("Welcome to Mr. Gallo's fantastic birth-o-meter!")
    print()
    print("All you have to do is enter your birthday, and it will tell you")
    print("the day of the week on which you were born.")
    print()
    print("Some automatic tests....")
    print(f"12 10 2003 => {weekday(12, 10, 2003)}")  # Wednesday, December 10, 2003
    print(f"2 13 1976 => {weekday(2, 13, 1976)}")  # Friday, February 13, 1976
    print(f"2 13 1977 => {weekday(2, 13, 1977)}")  # Sunday, February 13, 1977
    print(f"7 2 1974 => {weekday(7, 2, 1974)}")  # Tuesday, July 2, 1974
    print(f"1 15 2003 => {weekday(1, 15, 2003)}")  # Wednesday, January 15, 2003
    print(f"10 13 2000 => {weekday(10, 13, 2000)}")  # Friday, October 13, 2000

    print("Now it's your turn!  What's your birthday?")
    print("Birth date (mm dd yyyy): ")
    mm = int(input("mm: "))
    dd = int(input("dd: "))
    yyyy = int(input("yyyy: "))
    
    birthday = weekday(mm, dd, yyyy)
    print(f"\nYou were born on {birthday}!")



def weekday(mm: int, dd: int, yyyy: int) -> str:
    years_since_1900 = yyyy - 1900
    total = years_since_1900 // 4 + years_since_1900 + dd + month_offset(mm)

    # steps 3-7 go here

    if is_leap(yyyy) and (mm == 1 or mm == 2):
        total -= 1

    remainder = total % 7

    weekday = weekday_name(remainder)

    date_string = f"{weekday} {month_name(mm)} {dd}, {yyyy}"  # step 8

    return date_string


# paste your functions from month_name, weekday_name, and month_offset here
def month_name(month: int) -> str:
    result = ""
    if month == 1:
        result = "January"
    elif month == 2:
        result = "February"
    elif month == 3:
        result = "March"
    elif month == 4:
        result = "April"
    elif month == 5:
        result = "May"
    elif month == 6:
        result = "June"
    elif month == 7:
        result = "July"
    elif month == 8:
        result = "August"
    elif month == 9:
        result = "September"
    elif month == 10:
        result = "October"
    elif month == 11:
        result = "November"
    elif month == 12:
        result = "December"
    else:
        result = "error"
    
    return result


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

def weekday_name(weekday: int) -> str:
    result = ""

    if weekday == 0:
        result = "Saturday"
    elif weekday == 1:
        result = "Sunday"
    elif weekday == 2:
        result = "Monday"
    elif weekday == 3:
        result = "Tuesday"
    elif weekday == 4:
        result = "Wednesday"
    elif weekday == 5:
        result = "Thursday"
    elif weekday == 6:
        result = "Friday"
    else:
        result = "error"

    return result

def is_leap(year: int) -> bool:
    # years which are evenly divisible by 4 are leap years,
    # but years divisible by 100 are not leap years,
    # though years divisible by 400 are leap years

    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    
    return result


if __name__ == "__main__":
    main()