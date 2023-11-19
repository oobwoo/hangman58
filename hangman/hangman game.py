import random
#Import 



class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        
        word_guessed = self.word_guessed
        num_letters = self.word_guessed
        
        print(f"The mystery word has: {num_letters}")
        print(word_guessed)
    
    def check_guess(self, guess):
        # have kept the wording from milestone_4 check_guess as supposed to check_letter
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        #have kept wording from milestone_4 ask_for_input not ask_letter
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
            
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 2:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break  
#task 1 coding the logic to the hangman game
def play_game(word_list):
    num_lives = 5 #setting the number of lives
    game = Hangman(word_list, num_lives) # passing arguments

    while True:
        if game.num_lives == 0: #checks number of lives if 0 then game lost 
            print(f"You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            # asking for input then showing and overview of how the game is going 
            print("Word guessed so far:", game.word_guessed)
            print("List of guesses:", game.list_of_guesses)
            print("Number of letters left:", game.num_letters)
            print("Number of lives left:", game.num_lives)
        else:
            print("Congratulations. You won the game!")
            break
#from hangman template file adding words in list and calling the function
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%