from data import resources
from data import MENU
from data import coffee_price


def coffees(coffee,):
    menu_water = MENU[coffee]['ingredients']['water']
    resources_water = resources['water']
    menu_milk = MENU[coffee]['ingredients']['milk']
    resources_milk = resources['milk']
    menu_coffee = MENU[coffee]['ingredients']['coffee']
    resources_coffee = resources['coffee']
    final_water = resources_water - menu_water
    final_milk = resources_milk - menu_milk
    final_coffee = resources_coffee - menu_coffee
    if final_coffee < 0:
        print("Sorry, there's not enough coffee")
        return False
    elif final_water < 0:
        print("Sorry, there's not enough water")
        return False
    elif final_milk < 0:
        print("Sorry, there's not enough milk")
        return False
    else:
        resources['water'] = final_water
        resources['milk'] = final_milk
        resources['coffee'] = final_coffee


def price(coffee,):
    print("Please insert coins")
    quarters = (int(input("How many quarters? "))) / 4
    dimes = (int(input("How many dimes? "))) / 10
    nickels = (int(input("How many nickels? "))) / 20
    pennies = int(input("How many pennies? ")) / 100
    sum_money = quarters + dimes + nickels + pennies

    change = sum_money - coffee_price[coffee]
    if change < 0:
        print("Your money isn't enough. Your money has been refunded.")
    else:
        print("Here's your cup of coffee. Enjoy.")
        resources['money'] += coffee_price[coffee]
        print(f"Here's your ${change} change")


start = True
while start:
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if question == 'off':
        start = False
        print("Program has ended")
    elif question == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml ")
        print(f"Coffee: {resources['coffee']}g\nMoney: ${resources['money']} ")
    elif question == 'espresso':
        coffees('espresso')
        if coffees('espresso'):
            price('espresso')
        else:
            start = False
    elif question == 'latte':
        coffees('latte')
        if coffees('espresso'):
            price('latte')
        else:
            start = False
    elif question == 'cappuccino':
        coffees('cappuccino')
        if coffees('espresso'):
            price('cappuccino')
        else:
            start = False

    else:
        print("Sorry, you seem to have entered an invalid coffee, try again")