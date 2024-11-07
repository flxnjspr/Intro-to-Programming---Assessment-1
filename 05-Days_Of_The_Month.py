# 05: Days Of The Month

from datetime import datetime  # Importing only the datetime class to avoid unnecessary module import

# Function to determine the number of days in a given month, considering leap years if a year is provided
def get_days_in_month(month, year=None):
    # Dictionary storing the standard number of days for each month
    months_and_days = {
        1: 31,   # January
        2: 28,   # February (default non-leap year)
        3: 31,   # March
        4: 30,   # April
        5: 31,   # May
        6: 30,   # June
        7: 31,   # July
        8: 31,   # August
        9: 30,   # September
        10: 31,  # October
        11: 30,  # November
        12: 31   # December
    }

    # Checking if the month is February and a year is provided to determine if it's a leap year
    if month == 2 and year is not None:
        # Leap year check: divisible by 4 and not by 100, or divisible by 400
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29  # February has 29 days in a leap year

    # Return the number of days for the given month or None if the month is invalid
    return months_and_days.get(month)

# Function to get a valid year from user input or return the current year if input is blank or invalid
def get_year_input():
    year_input = input("Enter the year (or press Enter for the current year): ").strip()
    if year_input.isdigit():  # Check if the input is a valid digit
        return int(year_input)  # Convert the valid input to an integer and return it
    else:
        print("Invalid year input, using current year.")  # Feedback for invalid year input
        return datetime.now().year  # Use the current year as default if input is invalid

# Main function to prompt the user for month and year, then display the number of days in that month
def main():
    while True:  # Infinite loop to repeatedly ask for valid month input
        search = input("Enter the number of the month (1-12): ").strip()  # Prompt user for month number

        # Check if the input is a valid month number (1-12)
        if search.isdigit():  # Check if the input is a number
            month = int(search)  # Convert the month to an integer
            if 1 <= month <= 12:  # Ensure the month is within the valid range
                year = get_year_input()  # Get the year input from the user
                days = get_days_in_month(month, year)  # Get the number of days for the month and year

                # If the month is valid and days is not None, display the result
                if days is not None:
                    print(f"The number of days in month {month} of year {year} is: {days}")
                    break  # Exit the loop after a valid entry
                else:
                    print("There was an error calculating the number of days.")
            else:
                print("That input is invalid. Please enter a valid number between 1 and 12.")  # Clarified input error message
        else:
            print("That input is invalid. Please enter a valid number (1-12).")  # For non-numeric input

# Check if the script is run directly and not imported, then call the main function
if __name__ == "__main__":
    main()
