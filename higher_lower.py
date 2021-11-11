import random
from art import logo, vs
from game_data import data

score = 0
tries = 0

#show logo
print(logo)

while score < 10:
    tries += 1
    #ask user to compare two entries from data
    random_one = random.choice(list(data))
    random_two = random.choice(list(data))
    # 'Compare {random entry 1}'
    print(f'Compare A: {random_one["name"]}, a {random_one["description"]} from {random_one["country"]}')
    ####    #show vs sign
    print(vs)
    ##### 'to {random entry 2}'
    print(f'Against B: {random_two["name"]}, a {random_two["description"]} from {random_two["country"]}')
    ####Ask user who has more follower
    answer = input(f'Who do you think has more followers? Type either A or B:\n').lower()
    if answer == 'a':
        if random_one['follower_count'] > random_two['follower_count']:
            score += 1
            print(f'You\'re right! Current score: {score}\n')
        else:
            print(f'You\'re wrong! Current score: {score}\n')
    elif answer == 'b':
        if random_two['follower_count'] > random_one['follower_count']:
            score += 1
            print(f'You\'re right! Current score: {score}\n')
        else:
            print(f'You\'re wrong! Current score: {score}\n')
    #remove the previous dicts from list to prevent duplicates
    for person in data:
        if person['name'] == random_one['name']:
            data.remove(person)
        elif person['name'] == random_two['name']:
            data.remove(person)
        
if score == 10:
    print(f'It took you {tries} tries to get {score} right. Congrats!\n')
