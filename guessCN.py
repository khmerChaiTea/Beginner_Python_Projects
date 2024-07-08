# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

import random # A random package with it own functions, like random.randint
import math

# Defined a function to get a random int as a parameter, between 1 and 'x' number
def guess(x):
    random_number = random.randint(1, x)
    guess = 0 # Initialize guess
    max_guesses = math.ceil(math.sqrt(x))  # Calculate max_guesses as sqrt(x), rounded up
    num_guesses = 0  # Initialize the counter for number of guesses
    
    # Use a 'while' loop with an '(expression)' since we do not have pre-defined iteration
    while guess != random_number:
        if num_guesses < max_guesses:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            num_guesses += 1  # Increment the guess counter
        
            # Use 'if/else' statements to let the user know if the guess is too low or too high
            if guess < random_number:
                print('Sorry, guess again. Too low')
            elif guess > random_number:
                print('Sorry, guess again. Too high')
        else:
            print(f"Sorry, you've exceeded the maximum number of guesses ({max_guesses}). The correct number was {random_number}.")
            return  # Exit the function since max guesses exceeded
    
    print(f"Congratulations! You have guessed the number {random_number} correctly in {num_guesses} guesses.")
        
nth_range = int(input(f'Please enter a number for the largest range: '))
guess(nth_range)