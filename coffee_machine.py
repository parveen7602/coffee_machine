Menu={
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":200,
            "milk":200,
         },
        "cost":150
     },
    "espresso":{
        "ingredients":{
            "water":59,
            "coffee":37,
            "milk":40,
         },
        "cost":120
     },
    "capuccino":{
        "ingredients":{
            "water":80,
            "coffee":60,
            "milk":40,
         },
        "cost":170
     }
}
profit=0
resources={
    "water":500,
    "coffee":450,
    "milk":400
}
def check_resources(order_resources):
    for item in order_resources:
        if order_resources[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def process_coins():
    print("Please insert coins")
    total=0
    coins_five=int(input("how many 5rs coins?:"))
    coins_ten=int(input("how many 10rs coins?:"))
    coins_twenty=int(input("how many 20rs coins?:"))
    total=coins_five*5 + coins_ten*10 + coins_twenty*20
    return total
def is_payment_successful(money_received,coffee_cost):
    global profit
    if money_received >= coffee_cost:
        profit += coffee_cost
        change = money_received-coffee_cost
        print(f"here is your Rs {change} remaining.")
        return True
    else:
        print("sorry that's not enough money.money refunded")
        return False
def make_coffee(coffee_name,coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"here is your {coffee_name}☕..enjoy!!")
is_on=True
while is_on:
    choice=input("what Would you like to have?(latte/espresso/capuccino)?:")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water={resources['water']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"milk={resources['milk']}ml")
        print(f"money:rs{profit}")
    else:
        coffee_type= Menu[choice]
        if check_resources(coffee_type["ingredients"]):
            payment=process_coins()
            if is_payment_successful(payment,coffee_type["cost"]):
                make_coffee(choice,coffee_type["ingredients"])
            else:
                print("sorry that's not enough money.money refunded")