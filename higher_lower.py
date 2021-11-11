import random
from art import logo, vs
from game_data import data
def play():
    #show logo
    print(logo)
    #set variable of score equal to 0 as an official restart of score
    score = 0
    tries = 0
    while score < 10:
        tries += 1
        #ask user to compare two entries from data
        random_one = random.choice(list(data))
        random_two = random.choice(list(data))
        # 'Compare {random entry 1}'
        print(f'Compare A: {random_one["name"]}, a {random_one["description"]} from {random_one["country"]}\n')
        ####    #show vs sign
        print(vs)
        ##### 'to {random entry 2}'
        print(f'Against B: {random_two["name"]}, a {random_two["description"]} from {random_two["country"]}\n')
        ####Ask user who has more follower
        answer = input(f'Who do you think has more followers? Type either A or B: \n').lower()
        if answer == 'a':
            if random_one['follower_count'] > random_two['follower_count']:
                score += 1
                print(f'You\'re right!\nCurrent score: {score}\n')
            else:
                print(f'Sorry, but that\'s wrong!\nCurrent score: {score}\n')
        elif answer == 'b':
            if random_two['follower_count'] > random_one['follower_count']:
                score += 1
                print(f'You\'re right!\nCurrent score: {score}\n')
            else:
                print(f'Sorry, but that\'s wrong!\nCurrent score: {score}\n')
        #remove the previous dicts from list to prevent duplicates
        for person in data:
            if person['name'] == random_one['name']:
                data.remove(person)
            elif person['name'] == random_two['name']:
                data.remove(person)
            
    if score == 10:
        print(f'It took you {tries} tries to get {score} answers right. Good job!\n')
    replay = int(input('Type 1 to replay. Type 2 otherwise.\n'))
    if replay == 1:
        play()

play()
