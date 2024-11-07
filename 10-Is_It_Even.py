# Exercise 10: Is It even?

# Creating function to determine if the number is odd or even
def check_even_odd(number):
    if number % 2 == 0:  # Check if the number is divisible by 2
        return "The number is even."  # Return message for even number
    else:
        return "The number is odd."  # Return message for odd number

# Main function
def main():
    user_input = input("Please enter a number: ")  # Prompt the user for a number
    try:
        number = int(user_input)  # Convert input to an integer
        result = check_even_odd(number)  # Call the function to check if the number is even or odd
        print(result)  # Print the message returned by the function
    except ValueError:
        print("That's not a valid number. Please enter an integer.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Call the main function to execute the program
