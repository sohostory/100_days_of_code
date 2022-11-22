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


def check_resource(needed):
    if resources['water'] < needed['water']:
        print("Sorry there is not enough water.")
        return False
    elif resources['milk'] < needed['milk']:
        print("Sorry there is not enough milk.")
        return False
    elif resources['coffee'] < needed['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def coffee_recipe(coffee_name, name):
    return coffee_name[name]


def insert_coin():
    print("Please insert coins.")
    money_in = 0.00
    money_in += float(input("how many quarters?: "))*0.25
    money_in += float(input("how many dimes?: "))*0.10
    money_in += float(input("how many nickles?: ")) * 0.05
    money_in += float(input("how many pennies?: "))*0.10
    return money_in


def return_change(inserted, need):
    return inserted - need


def make_coffee(coffee):
    print(f"Here us your {coffee} ☕. Enjoy!")


def print_report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


machine_on = True
money_in_machine = 0.00
milk_needed = 0

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':
        print_report(resources["water"], resources["milk"], resources["coffee"], money_in_machine)
    else:
        coffee_choice = MENU[user_choice]
        coffee_ingredients = coffee_choice["ingredients"]
        resource_needed = {"water": 0, "milk": 0, "coffee": 0}
        for key in coffee_ingredients:
            resource_needed[key] = coffee_recipe(coffee_ingredients, key)

        money_needed = coffee_choice['cost']

        if check_resource(resource_needed):
            money_inserted = insert_coin()
            if money_inserted < money_needed:
                print("Sorry that's not enough money. Money refunded.")
            elif money_inserted > money_needed:
                change = return_change(money_inserted, money_needed)
                print(f"Here is ${round(change, 2)} in change.")
                make_coffee(user_choice)
                money_in_machine += money_needed
                for key in coffee_ingredients:
                    resources[key] -= coffee_ingredients[key]
            else:
                make_coffee(user_choice)
                money_in_machine += money_needed
                for key in coffee_ingredients:
                    resources[key] -= coffee_ingredients[key]
