import random
from art import logo, vs
from game_data import data

#show logo
print(logo)
#ask user to compare two entries from data
# 'Compare {random entry 1}'
random_one = random.choice(list(data))
print(f'Compare A: {random_one["name"]}, a {random_one["description"]} from {random_one["country"]}')
##    #show vs sign
print(vs)
### 'to {random entry 2}'
random_two = random.choice(list(data))
print(f'Against B: {random_two["name"]}, a {random_two["description"]} from {random_two["country"]}')
##Ask user who has more follower
answer = input('Who do you think has more followers? Type either A or B: \n').lower()
#if user is wrong, return  ...
#else if user is right, return ...
##for person in data:
##    print(person['name'])
##    print(person['description'])
##    print(person['country'])
##    print(person['follower_count'])
