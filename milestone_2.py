import random

class milestone_2:


    word_list = ['apples', 'oranges', 'bananas', 'kiwis', 'pears']
    # print(word_list)
    
    def choice(word_list):
        return random.choice(word_list)
    
    word = random.choice(word_list)
    print(word)
    
guess = input("enter a single letter:  ")

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess)==1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# In the body of the if statement, print a message that says "Good guess!".


# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.