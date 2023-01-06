# Here you are importing the classes and modules that you need from the used packages:
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Here you are creating the objects from the imported classes:
coffee_maker = CoffeeMaker()  # manages the subtractions from resources based on the requested coffee and makes reports.
money_machine = MoneyMachine()  # manages the payments, analyzing if it's enough and adds the profit and makes reports.
menu = Menu()  # checks if the requested drink is in the list, how many ingredients they need, and its price

run = True

while run:
    # Besides creating objects you also have to create variables to control their individual methods and attributes.
    # Here you created the option variable to control the get_item method, which shows the available drinks:
    options = menu.get_items()

    request = input(f"What would you like? {options}: ")
    if request == "off":
        print("Bye! ")
        run = False
    elif request == "report":
        coffee_maker.report()
        money_machine.report()
        print(" ")
# The next lines of code were particularly difficult for me because I needed to create new variables to control
# the methods and I also needed to feed the methods with those variables. I also didn't know that
# those new variables where connected to the objects previously created, and therefore they also had the
# possibility to use their methods and attributes:
    else:
        drink = menu.find_drink(request)
        if drink:
            enough = coffee_maker.is_resource_sufficient(drink)
            if enough:
                enough_money = money_machine.make_payment(drink.cost)
                if enough_money:
                    coffee_maker.make_coffee(drink)
                    print(" ")
        elif request != drink:
            print(" ")
