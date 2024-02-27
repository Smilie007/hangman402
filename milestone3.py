import random
class Milestone3:
    word_list = ['apples', 'oranges', 'bananas', 'kiwis', 'pears']
    word = random.choice(word_list)
    
    print(word)

def check_guess(guess, word):
  guess =  guess.lower()
  if guess.isalpha() and len(guess)==1:
    if word.__contains__(guess):
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

        
  else:
    print("Invalid letter. Please, enter a single alphabetical character.")
    return False     

def ask_for_input():
        while True:
          word = Milestone3.word
          guess = input("Guess a letter: ")
          print("You entered: " + guess) 
          if check_guess(guess, word):
             break

ask_for_input()
            
 
            