import random

# task 2 below
word_list = ["grape", "peach", "mango", "melon", "cherry"]

word = random.choice(word_list)
print(word)

# task 3 below
guess = input("Enter a single letter")

if len(guess) == 1 and guess.isalpha():
    print ("Good Guess!")

else: 
    print ("Oops! That is not a valid input.")