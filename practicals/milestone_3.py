import random
#milestone_3 - Check if guessed character is in the word
# setting the word list adding 5 my randoms fruits
word_list = ["apple", "banana", "orange", "strawberry", "kiwi"]

#Task 3 creating functions adding task 1 & 2 codes into functions
def check_guess(guess):
    
    guess = guess.lower()

    #task 2 check whether guess is in word
    if guess in guess_word:
        
        print(f"Good guess! '{guess}' is in the word.")
    else:
        
        print(f"Sorry, '{guess}' is not in the word. Try again.")


def ask_for_input():
    #task 1 Iteratively check if the input is a valid guess
    while True:
        
        guess = input("Guess a letter: ")
        
        if len(guess) == 1 and guess.isalpha():
            # break out of loop if conditions are met
            break
        else:
            # if not a valid input return message
            print("Invalid letter. Please, enter a single alphabetical character.")

    # calling function to check guess to guess word
    check_guess(guess)

#random selection from word list
guess_word = random.choice(word_list)

# checking code by calling function and revealing the guess word
ask_for_input()
print(f"The word was: {guess_word}")