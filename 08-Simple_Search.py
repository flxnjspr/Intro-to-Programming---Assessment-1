# Exercise 8: Simple Search

# List of names to search through
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Prompt the user to enter a name, remove any leading/trailing spaces, and convert it to lowercase for case-insensitive matching
search = input("Enter the name you want to search for: ").strip().lower()

# Check if the lowercase version of the input matches any lowercase version of names in the list
if search in [name.lower() for name in names]:
    # If a match is found, print confirmation with the name capitalized for readability
    print(f"We have the name {search.capitalize()} on our list! ")
else:
    # If no match is found, inform the user and display the entered name capitalized
    print(f"Sorry. We don't have {search.capitalize()} on our list. ")
