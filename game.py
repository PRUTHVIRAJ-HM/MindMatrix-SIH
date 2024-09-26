# game.py

import random

def play_game(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = ""

    if user_choice not in choices:
        return "Invalid choice! Please choose rock, paper, or scissors."

    if user_choice == computer_choice:
        result = f"Both chose {user_choice}. It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = f"You chose {user_choice}, computer chose {computer_choice}. You win!"
    else:
        result = f"You chose {user_choice}, computer chose {computer_choice}. Computer wins!"

    return result
