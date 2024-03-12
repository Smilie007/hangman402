import random

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' ] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        #print(self.word)

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self.update_word_guessed(guess)
        else:    # Step 1: Create an else statement
            self.reduce_guess_lives(guess)

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):   #go through each letter in word
            if letter == guess:  # Check if the letter matches the guess
                self.word_guessed[i] = guess  # Replace the corresponding "_" in word_guessed with the guess
                self.num_letters -= 1  # Reduce the variable num_letters by 1
                self.num_letters = self.word_guessed.count('_') #counts the number of letters that have not been guessed yet
                
    def reduce_guess_lives(self, guess):
        self.num_lives -= 1   # Step 2.1: Reduce num_lives by 1
        print(f"Sorry, {guess} is not in the word.")    # Step 2.2: Print a message for incorrect guess
        print(f"You have {self.num_lives} lives remaining.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

word_list = ['apple', 'banana', 'orange', 'grape', 'kiwi']
play_game(word_list)