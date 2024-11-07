# 03 - Biography


name = input("What is your name?: ")  # Prompt the user for their name and storing it in the variable 'name'

hometown = input("What is your hometown?: ")  # Prompt user for their hometown and storing it in the variable 'hometown'

while True:  # Loop that will repeatedly ask for age until a valid integer is entered
    try:
        age = int(input("What is your age?: "))  # Prompt user for their age and store it in the variable 'age'
        # converting user input to an integer

        break  # Exit loop if conversion is successful

    except ValueError:

        print(
            "Invalid input for age. Please input a valid number.")  # Informing the user IF input is not a valid integer

info = {"Name": name, "Hometown": hometown, "Age": age}  # Store the gathered information in a dictionary 'info'

for key, value in info.items():  # Iterating through the values in the dictionary and print each one
    print(f"{key}: {value}")  # Using f-string for cleaner output formatting