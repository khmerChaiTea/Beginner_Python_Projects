# 12 Beginner Python Projects with https://www.youtube.com/watch?v=8ext9G7xspg&ab_channel=freeCodeCamp.org

import random

def play():
    while True:
        user = input("Let's Play Rock, Paper, Scissors! Please type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
        
        if user not in ['r', 'p', 's']:
            print("Invalid input! Please type 'r', 'p', or 's'.")
        else:
            break # Break out of the loop when valid input is received
        
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost'
    
def is_win(player, opponent):
    # Return true if the player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    return False
    
print(play())