# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words) # Randomly chooses something from the words list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    
    lives = 10 # Start with 10 lives
    
    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        print(lives_visual_dict[lives]) # Display current hangman visual
        
        # Letters used
        # ' '.join(['a','b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters, please enter a letter: ', ' '.join(used_letters))
        
        # Current word display (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # Decrease life count if the guess is wrong
                print('Letter is not in the word.')
                if lives == 0:
                    # Display final hangman visual when lives reach 0
                    print(lives_visual_dict[0])
                    break # Break out of the loop if lives reach 0
                
        elif user_letter in used_letters:
            print('You have already guess that character. Please try again.')
            
        else:
            print('Invalid character. Please try again.')
            

            
    # End of game message, gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('Sorry, you died. The word was', word)
    else:
        print('Congratulations! You guessed the word', word, '!!')

# Call the hangman function to start the game            
hangman()