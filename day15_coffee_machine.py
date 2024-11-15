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
    "profit": 0
}

# TODO : Check resources.
def check_resources(drink):
    for ingredient in MENU[drink]['ingredients'].keys():
        if resources[ingredient] < MENU[drink]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

# TODO : Process coins.
def process_coins(quarters,dimes,nickels,pennies):
    return quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01

# TODO : Check transaction.
def check_transaction(money,drink):
    drink_cost = MENU[drink]['cost']
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        resources['profit'] += drink_cost
        print(f"Here is ${change} in change")
        return True

    else:
        print("Sorry that's not enough money. Money refunded")
        return False

# TODO : Make coffee.

def make_coffee(drink):
    for ingredient in MENU[drink]['ingredients'].keys():
        resources[ingredient] -= MENU[drink]['ingredients'][ingredient]
    return f"Here is your {drink} ☕. Enjoy!"

# TODO : Prompt user by asking "What would you like?"

machine_on = True

while machine_on:
    choice = input("What would you like? (Espresso 1.5$ / Latte 2.5$ / Cappuccino 3.0$): ").lower()

# TODO : Turn off the Coffee Machine by entering "off" to the prompt.
    if choice == "off":
        machine_on = False

# TODO : Print report by entering "report" to the prompt.
    elif choice == "report":
        print(f"Water: {resources['water']} ml\n"
              f"Milk: {resources['milk']} ml\n"
              f"Coffee: {resources['coffee']} g\n"
              f"Money: {resources['profit']}")

    elif check_resources(choice):
        print("Please insert coins.")
        quarters = int(input("How many quarters?:"))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        payment = process_coins(quarters,dimes,nickles,pennies)

        if check_transaction(payment,choice):
            print(make_coffee(choice))
    else:
        print("There are not enough resource for the drink!")
