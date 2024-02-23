"""
    Schere, Stein, Papier
"""

import random, time

moves = ['Scissors', 'Stone', 'Paper']

print('Hello and welcome to this game.')

user_points = 0
machine_points = 0

while user_points or machine_points < 3:
    user_choose = input('Choose one item: Scissors, Stone or Paper? ')
    print(user_choose)

    print('...')
    time.sleep(2)

    machine_choose = random.choice(moves)
    print(f"Ok... I've got '{machine_choose}'!")

    if user_choose == machine_choose:
        print(f'It\'s a draw!\nYour score: {user_points}'); print(f'My score: {machine_points}')
    elif user_choose == 'Scissors':
        if machine_choose == 'Stone':
            print('I win!')
            machine_points += 1
            print(f'Your score: {user_points}'); print(f'My score: {machine_points}')
        elif machine_choose == 'Paper':
            print('You win!')
            user_points += 1
            print(f'Your score: {user_points}'); print(f'My score: {machine_points}')
    elif user_choose == 'Stone':
        if machine_choose == 'Scissors':
            print('You win!')
            user_points += 1
            print(f'Your score: {user_points}'); print(f'My score: {machine_points}')
        elif machine_choose == 'Paper':
            print('I win!')
            machine_points += 1
            print(f'Your score: {user_points}'); print(f'My score: {machine_points}')
    elif user_choose == 'Paper':
        if machine_choose == 'Scissors':
            print('I win!')
            machine_points += 1
            print(f'Your score: {user_points}'); print(f'My score: {machine_points}')
        elif machine_choose == 'Stone':
            print('You win!')
            user_points += 1
            print(f'Your score: {user_points}'); print(f'My score: {machine_points}')
    
    if user_points == 3:
        print(f'Congratulations, you won the game!\nThe score is {user_points} - {machine_points}.')
        break
    elif machine_points == 3:
        print(f'Oh, looks like that I won this game!\nThe score is {user_points} - {machine_points}.')
        break
