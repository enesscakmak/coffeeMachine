# Coffe Machine for 100 Days of Code Python Course

# a list with dictionaries for coffees
# a function to take money, deduct it, give rest if it's much and return the remaining money in machine
# a function to check if resources are sufficient for the request and give coffee if it is
# all operations should be in a while loop  until off turns True

ingredients = {"espresso": {"water": 100, "milk": 100, "coffee": 100},
               "latte": {"water": 100, "milk": 200, "coffee": 50},
               "cappuccino": {"water": 100, "milk": 50, "coffee": 150},
               }

cost = {"espresso": 2.5,
        "latte": 3,
        "cappuccino": 4
        }

resources = {"water": 1000,
             "milk": 1000,
             "coffee": 1000,
             "money": 10
             }

coins = {"quarter": 0.25,
         "dime": 0.10,
         "nickel": 0.05,
         "pennie": 0.01
         }


def takeOrder():
    order = input("What would you like? Enter 'espresso', 'latte' or 'cappuccino' for your request:")
    while order != "off":
        makeCoffee(order)
        order = input("What else would you like? Enter 'espresso', 'latte', or 'cappuccino' for your request:")
    else:
        exit()


def money(totalMoney, order):
    if totalMoney < cost[order]:
        print("Sorry, that's not though money. Money refunded.")
        takeOrder()
    elif totalMoney > cost[order]:
        excessiveMoney = totalMoney - cost[order]
        print(f"Transaction completed, here is your change of {excessiveMoney:.2f}. Enjoy your {order} 🙂.")
        resources["money"] += totalMoney - excessiveMoney
        lessenResources(order)
    elif totalMoney == cost[order]:
        print(f"Transaction completed. Enjoy your {order} 🙂.")
        resources["money"] += totalMoney
        lessenResources(order)


def makeCoffee(order):
    if order in ingredients:
        requiredIngredients = ingredients[order]
        for ingredient, amount in requiredIngredients.items():
            if resources[ingredient] < amount:
                print(f"Sorry there is not enough {ingredient}")
                break
            else:
                print(f"{order} cost", cost[order], "please select the amount you will enter⬇")
                quarters = int(input("Enter the amount of quarters you will give:"))
                dimes = int(input("Enter the amount of dimes you will give:"))
                nickles = int(input("Enter the amount of nickles you will give:"))
                pennies = int(input("Enter the amount of pennies you will give:"))
                totalMoney = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
                money(totalMoney, order)
                break


def lessenResources(order):
    requiredIngredients = ingredients[order]
    for ingredient, ingredientAmount in requiredIngredients.items():
        resources[ingredient] -= ingredientAmount
    print(resources)


takeOrder()


