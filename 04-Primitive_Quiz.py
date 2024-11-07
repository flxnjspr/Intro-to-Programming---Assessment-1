# 4 - primitive quiz

# Print a welcome message indicating the start of the quiz about European capitals
print("Today you will be answering 10 questions about the capitals of 10 European countries! Let's start.")

# Dictionary containing countries as keys and their corresponding capitals as values
countries = {
    "France": "paris",           # Declaring France as key and Paris as value
    "Poland": "warsaw",          # Declaring Poland as key and Warsaw as value
    "United Kingdom": "london",  # Declaring United Kingdom as key and London as value
    "Germany": "berlin",         # Declaring Germany as key and Berlin as value
    "Spain": "madrid",           # Declaring Spain as key and Madrid as value
    "Finland": "helsinki",       # Declaring Finland as key and Helsinki as value
    "Greece": "athens",          # Declaring Greece as key and Athens as value
    "Italy": "rome",             # Declaring Italy as key and Rome as value
    "Netherlands": "amsterdam",  # Declaring Netherlands as key and Amsterdam as value
    "Ireland": "dublin"          # Declaring Ireland as key and Dublin as value
}


for country, capital in countries.items(): # Loop through each country and its corresponding capital in the countries dictionary
    
    answer = input(f"What is the capital of {country}?: ").lower() # Prompt the user for the capital of the current country
                                                                   # Converting input to lowercase

    if answer == capital:       # Check if the user's answer matches the correct capital
        
        print("That is the correct answer!")   # Inform the user that their answer is correct

    else:
        
        print(f"That is the wrong answer! The correct answer is {capital.capitalize()}.")  # Inform the user that their answer is wrong and provide the correct capital
                                                                                            # .capitalize() to make the first letter of the city Capitalized
