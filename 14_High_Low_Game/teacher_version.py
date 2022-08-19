from art import logo, vs
from game_data import data
import random
from replit import clear

# Display art


# Format the ppl
def format_data(account):
    """Format the account data and return account info"""
    name = account["name"]
    descr = account["description"]
    country = account["country"]
    return f"{name}, a {descr}, from {country}"

def check_answer(a,b,guess):
    """Take the user guess and follower counts and return True if it is right"""
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_on = True
account_b = random.choice(data)

while game_on:
    # Generate a random ppl from game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers: A or B: ").lower()

    clear()
    # Compare the follower counts
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    is_correct = check_answer(a_followers, b_followers, guess)

    ## print out feedback
    if is_correct:
        score += 1
        print(f"You are right with score: {score}")
    else:
        print(f"Wrong, your current score is: {score}")
        game_on = False

    # Repeat the game
    # Replace ppl_B to ppl_A position
    # Compare ppl_B to ppl_B_new


