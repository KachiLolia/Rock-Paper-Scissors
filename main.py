import random

list_moves = ['r','p','s']

while True:
    user_input = input('Type r for Rock, p for Paper or s for Scissors, else Type Q tp quit: ').lower()

    if user_input == 'q':
        break
    if user_input not in list_moves:
        print("Error, please select a valid option")
        continue

    computer_choice = random.choice(list_moves)

    if user_input == computer_choice:
        print('Player: {} CPU: {}. Its a tie!'.format(user_input.capitalize(),computer_choice.capitalize()))
        continue

    if (user_input == 'r' and computer_choice == 's') or (user_input == 'p' and computer_choice == 'r') or (user_input == 's' and computer_choice == 'p'):
        print("Player: {} CPU: {}. You Win!!".format(user_input.capitalize(),computer_choice.capitalize()))
        break

    else:
        print("Player: {} CPU: {}. You Lose!!, Computer Wins!!".format(user_input.capitalize(),computer_choice.capitalize()))
        continue
