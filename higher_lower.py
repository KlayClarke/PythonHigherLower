import os
import random
from art import logo, vs
from game_data import data

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def play():
    clear_console()
    #show logo
    print(logo)
    #set variable of score equal to 0 as an official restart of score
    score = 0
    tries = 0
    random_account_b = random.choice(list(data))
    while score < 10:
        tries += 1
        #ask user to compare two entries from data
        random_account_a = random_account_b
        random_account_b = random.choice(list(data))
        # 'Compare {random entry 1}'
        print(f'Compare A: {random_account_a["name"]}, a {random_account_a["description"]} from {random_account_a["country"]}\n')
        ####    #show vs sign
        print(vs)
        ##### 'to {random entry 2}'
        print(f'Against B: {random_account_b["name"]}, a {random_account_b["description"]} from {random_account_b["country"]}\n')
        #remove the previous dicts from list to prevent duplicates
        for person in data:
            if person['name'] == random_account_a['name']:
                data.remove(person)
            elif person['name'] == random_account_b['name']:
                data.remove(person)
        ####Ask user who has more follower
        answer = input(f'Who do you think has more followers? Type either A or B: \n').lower()
        #clear screen
        clear_console()
        print(logo)
        if answer == 'a':
            if random_account_a['follower_count'] > random_account_b['follower_count']:
                score += 1
                print(f'You\'re right!\nCurrent score: {score}\n')
            else:
                print(f'Sorry, but that\'s wrong!\nCurrent score: {score}\n')
        elif answer == 'b':
            if random_account_b['follower_count'] > random_account_a['follower_count']:
                score += 1
                print(f'You\'re right!\nCurrent score: {score}\n')
            else:
                print(f'Sorry, but that\'s wrong!\nCurrent score: {score}\n')
            
    if score == 10:
        print(f'It took you {tries} tries to get {score} answers right. Good job!\n')

    replay = int(input('Type 1 to replay. Type 2 otherwise.\n'))
    if replay == 1:
        play()
    else:
        print('Goodbye!')

play()
