import random
# TODO 1: Set target number as a ramdom num
# TODO 2: Choose difficulty level
# TODO 3: If the level is 'hard'-> temp = 5
#         Else (easy) -> temp = 10
# TODO 4: Start_guess function in 'temp loop'
#         Compare the guess to target


target = random.randint(1, 100)
go_on = True

def start_guess():
    global temp
    #global go_on # if NOT global or has no this statement, program will NOT end after you guess the right number

    while go_on:
        if temp != 0:
            guess = int(input('Make a guess: '))
            if guess < target:
                #temp = temp - 1  # temp is 0 if use temp -= temp
                temp -= temp
                print(f'Too Low.\nGuess again.\nYou have {temp} attempts remaining to guess the number.')
            elif guess > target:
                #temp = temp - 1
                temp -= temp
                print(f'Too High.\nGuess again.\nYou have {temp} attempts remaining to guess the number.')
            else:
                print(f'You got it! The answer was {target}')
                #go_on = False  # go_on is still True here
                return 1
        else:
            return 1



print('Welcome to the NUMBER GUESSING game!')
print('I am thinking of a number between 1 and 100.')
print(f'Psst, the correct answer is {target}')
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == 'easy':
    temp = 10
    for i in range(0,temp):
        start_guess()
        if start_guess() == 1:
            break

else:
    temp = 5
    for i in range(0,temp):
        #start_guess()
        if start_guess() == 1:
            break