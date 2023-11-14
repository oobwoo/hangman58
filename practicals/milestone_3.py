import random

# List of random fruit for game
word_list = ["apple", "banana", "orange", "strawberry", "kiwi"]

# Function called check_guess
def check_guess(guess):
    #Converts the guess into lower case
    guess = guess.lower()

    #Check if the guess is in the word
    if guess in secret_word:
        #Print a success message
        print(f"Good guess! '{guess}' is in the word.")
    else:
        #Print a failure message
        print(f"Sorry, '{guess}' is not in the word. Try again.")

#Define a function called ask_for_input
def ask_for_input():
    #Create a while loop with the condition set to True
    while True:
        #Ask the user to guess a letter and assign it to a variable called guess
        guess = input("Guess a letter: ")

        #Check if the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Step 8: If the guess passes the checks, break out of the loop
            break
        else:
            # If the guess does not pass the checks, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

    #Call the check_guess function to check if the guess is in the word
    check_guess(guess)

#Code after the loop (e.g., game logic) goes here

#Randomly select a secret word from the list
secret_word = random.choice(word_list)

#Call the ask_for_input function to test code
ask_for_input()

#Print the actual secret word for testing purposes
print(f"The secret word was: {secret_word}")
