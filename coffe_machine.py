coffees={
    "latte":{"ingredients":{"water":100,"coffee":50,"milk":20},"cost":100},
    "espresso":{"ingredients":{"water":100,"coffee":50,"milk":20},"cost":100},
    "cappucino":{"ingredients":{"water":100,"coffee":50,"milk":20},"cost":100}
}
profit=0

report={
    "water":250,
    "milk":50,
    "coffee":250,
    "money":0
}
def check_stock(stock):
    for item in stock:
        if stock[item]>report[item]:
            print("sorry there is no enough ")
            return False
    return True
def collect_coins():
    total=0
    coins_5rs=int(input("please enter how many 5rs coins:"))
    coins_10rs=int(input("please enter how many 10rs coins:"))
    coins_20rs=int(input("please enter how many 20rs coins:"))
    total=coins_5rs*5 + coins_10rs*10 + coins_20rs*20
    return total
def is_payment_successfull(payment,coffee_cost):
    if payment>=coffee_cost:
        global profit
        profit += coffee_cost
        change=coffee_cost-payment
        print(f"here is your change{change}")
        return True
    else:
        print("there is no enough money")
        return False
def make_coffee(coffee, ingredients):
    global report
    for item in ingredients:
        report[item] -= ingredients[item]
    print(f"here is your {coffee}")


    
continue_checking=True
while continue_checking:
    choice=input("what would you like to have ?(latte/espresso/cappuccino)")
    if choice=="report":
        print(f"water:{report['water']} ml \nmilk:{report['milk']}ml \ncoffee:{report['coffee']}gm \nmoney:{report['money']}")
        continue_checking=True
    elif choice=="off":
        print("Good bye")
        continue_checking=False
    elif choice=="profit":
        print(profit)
    else:
        if choice in coffees:
            coffee_type=coffees[choice]
            if check_stock(coffee_type["ingredients"]):
                payment=collect_coins()
                if is_payment_successfull(payment,coffee_type["cost"]):
                    make_coffee(choice,coffee_type["ingredients"])
        else :
            print("invalid choice")
            continue_checking=True

