from art import logo, vs
from game_data import data
import random
from replit import clear

score = 0
print(logo)

def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def display():
    get_random_account()
    A = get_random_account()
    B = get_random_account()

    name_1 = A['name']
    description_1 = A['description']
    country_1 = A['country']
    count_1 = A['follower_count']
    print(f"Compare A: {name_1}, {description_1}, from {country_1}")
    print(vs)

    name_2 = B['name']
    description_2 = B['description']
    country_2 = B['country']
    count_2 = B['follower_count']
    print(f"Compare B: {name_2}, {description_2}, from {country_2}")

    if count_1 < count_2:
        return 'B'
    else:
        return 'A'


go_on = True
while go_on:
    print(f" == Current score: {score} == ")
    winner = display()
    guess = (input("Who has more followers? Type 'A' or 'B': "))

    if guess == winner:
        score += 1
        print(f"You're right! Current score: {score}")
        clear()
        if score == 50:
            break

    else:
        print(f"Sorry, that is wrong! Final score: {score}")
        go_on = False


