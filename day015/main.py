"""
Copy from main.py
"""
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


def start_coffee_machine(resources):
    current_profit = 0
    is_on = True

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice in ["off", "exit"]:
            is_on = False
            print("Bye!")
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${current_profit}")
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"], resources):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"], current_profit):
                    make_coffee(choice, drink["ingredients"], resources)


def is_resource_sufficient(order, remain_resource):
    for item in order:
        if order[item] > remain_resource[item]:
            print(f"Sorry not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost, profit):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients, resources):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


if __name__ == "__main__":
    start_coffee_machine(resources);
