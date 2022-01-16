from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start_coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    is_on = True
    while is_on:
        choice = input(f"What would you like? ({menu.get_items()}): ")
        if choice in ["off", "exit"]:
            is_on = False
            print("Bye!")
        elif choice == "report":
            coffee_maker.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    start_coffee_machine();
