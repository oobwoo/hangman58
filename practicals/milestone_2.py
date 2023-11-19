import random
#milestone_2 workings
#task 1
word_list = ["apple", "banana", "orange", "strawberry", "kiwi"]
print(word_list)

#task 2
word = random.choice(word_list)
print(word)

#task 3
guess = input("Please input single letter: ")

#task 4
if len(guess) == 1 and guess.isalpha():
    print("Good guess")

else:
    print("Oops! That's not a valid input")
    
