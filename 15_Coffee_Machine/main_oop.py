MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

income = 0


def calculate_coins():
    print("Please insert coins.")
    quas = int(input("how many quarters: "))
    dimes = int(input("how many dimes: "))
    nickles = int(input("how many nickles: "))
    pennies = int(input("how many pennies: "))
    total = float(quas * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)
    if total > MENU[choice]["cost"]:
        change = total - MENU[choice]["cost"]
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}. Enjoy!")

        global income
        income = income + MENU[choice]["cost"]
    else:
        print("Sorry that is not enough money. Money refunded.")

def has_resource(choice):
    if choice != "report":
      if (resources["water"] < MENU[choice]["ingredients"]["water"] or
         resources["milk"] < MENU[choice]["ingredients"]["milk"] or
         resources["coffee"] < MENU[choice]["ingredients"]["coffee"]):
           return False
      else:
          resources["water"] = resources["water"] - MENU[choice]["ingredients"]["water"]
          resources["milk"] = resources["milk"] - MENU[choice]["ingredients"]["milk"]
          resources["coffee"] = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
          return True
    else:
        print(f'Water: {resources["water"]} lm')
        print(f'Milk: {resources["milk"]} lm')
        print(f'Coffee: {resources["coffee"]} lm')
        print(f'Money: {income}')
        return True

def main():
    keep_order = True
    while keep_order:
       global choice
       choice = input(" What would you like? (espresso/latte/cappuccino/report)")
       if has_resource(choice):
           calculate_coins()
       else:
            break

main()
