# from replit import clear

# HINT: You can call clear() to clear the output in the console.
print("Welcome to the secret auction program.")

# TODO: COMPARE THE PRICE AND RETURN THE WINNER NAME

dic= {}
finish = False

def find_max(dic):
    max = 0
    winner = ""
    for bidder in dic:
        if dic[bidder] > max:
            max = dic[bidder]
            winner = bidder
    print(f'Winner is {winner} with price {max}')

# TODO: CREATE A DICT TO STORE NAME AND PRICE

while not finish:
    name = input("What is your name? ")
    price = int(input("What is your bid? "))
    dic[name] = price
    go_on = input("Are there any other bidders? Type 'yes' or 'no'.")
    if go_on == 'no':
        finish = True
        find_max(dic)
    else:
        print('CONTINUE-----')

'''
    finish = input("Are there any other bidders? Type 'yes' or 'no'.")
    if finish == 'no':
        finish = True
        find_max(dic)
    else:
        print(finish)  #printout 'yes', return to while condition and not able ot continue with 'yes'
        continue

'''




