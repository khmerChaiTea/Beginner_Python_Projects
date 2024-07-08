# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

import random # A random package with it own functions, like random.randint

# Defined a function to get a random int as a parameter, between 1 and 'x' number
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    count = 0  # Initialize a counter variable
    
    while feedback != 'c':
        if low <= high: # Ensure the range is valid
            guess = random.randint(low, high)
        else:
            raise ValueError("The range is empty! Check your logic.")  # Handle the case where low > high
            
        feedback = input(f'Is {guess} too hight (H), too low(L), or correct(C) ').lower()
        count += 1  # Increment the counter after each guess

        if feedback == 'h':
            high = guess - 1 # Adjust high to be one less than guess
        elif feedback == 'l':
            low = guess + 1 # Adjust low to be one more than guess
            
    print(f"Congratulations! The computer guessed your number, {guess}, correctly in {count} guesses.")

nth_range = int(input(f'Please enter a number for the largest range (Write down your secret number): '))
computer_guess(nth_range)