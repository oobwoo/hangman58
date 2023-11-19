import random
#milestone_5 have added class from milestone_4
class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
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
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
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
            print("You lost!")
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
