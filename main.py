from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()


options = menu.get_items()
choice = input(f"What would you like to have ({options})")
if choice == 'report':
