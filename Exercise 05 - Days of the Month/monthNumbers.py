# Create a dictionary with month numbers and days
month_days = {
    1: 31,
    2: 28,  # will adjust for leap year later
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for a month number
month = int(input("Enter the month number (1-12): "))

# Check if the input is valid
if month in month_days:
    # Confirm leap year if February is selected
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()

        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"Month {month} has {month_days[month]} days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
