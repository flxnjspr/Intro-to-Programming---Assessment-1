# 06 - Brute Force Attack

correct_password = "12345"  # The correct password
attempt = 0  # Initializes attempt counter
max_attempts = 5  # Maximum number of allowed attempts

while True:
    answer = input("Password: ")  # Prompt the user for the password
    if answer == correct_password:
        print("You are now logged in")  # Successful login message
        break  # Exit the loop if the correct password is entered
    else:
        attempt += 1  # Increment the attempt counter by 1
        attempts_remaining = max_attempts - attempt  # Calculate remaining attempts

        # Check if maximum attempts have been reached
        if attempts_remaining == 0:
            print("You have been suspicious and entered 5 incorrect passwords. The authorities have been alerted.")
            break  # Exit the loop after reaching maximum attempts
        else:
            # Inform the user of incorrect password and attempts remaining
            print(f"That is the incorrect password. You have {attempts_remaining} attempt/s remaining.")
