# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:32:46 2021

@author: Dean321
"""

machine = {
    "Espresso":{
        "water": 50,
        "milk": 0,
        "coffee": 18,
        "cost": 1.50
    },
    "Latte":{
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.50
    },
    "Cappuccino":{
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.00
    }
}
water = 300
milk = 200
coffee = 100
penny = 0.01
nickel = 0.05
dime = 0.10
quater = 0.25
choice = 0
selection = ""
def checkAvailabilty(c):
    if machine[c]["water"] <= water and machine[c]["milk"] <= milk and machine[c]["coffee"] <= coffee:
        return True
    else:
        return False
    

def collectCoins():
     p = int(input("Enter the number of pennies: "))
     n = int(input("Enter the number of nickles: "))
     d = int(input("Enter the number of dimes: "))
     q = int(input("Enter the number of quaters: "))
     return p, n, d, q

while choice!=7:
    choice = int(input(f"""
Coffee Vending Machine
Machine has Water - {water}\tMilk - {milk}\tCoffee - {coffee}
Choose your coffee option, type the number please
1 - Espresso
2 - Latte
3 - Cappuccino
4 - Add Milk
5 - Add Coffee
6 - Add Water
7 - Shutdown
And your choice is - """))
    if choice == 1:
        selection = "Espresso"
    elif choice == 2:
        selection = "Latte"
    elif choice == 3:
        selection = "Cappuccino"
    elif choice == 4:
        qty = int(input("Enter the quatity you wish to add"))
        milk += qty
    elif choice == 5:
        qty = int(input("Enter the quatity you wish to add"))
        coffee += qty
    elif choice == 6:
        qty = int(input("Enter the quatity you wish to add"))
        water += qty
    else:
        print("Incorrect Input. Try Again")
    if selection != "":
        if checkAvailabilty(selection):
            p, n, d, q = collectCoins()
            total = (penny * p) + (nickel * n) + (dime * d) + (quater * q)
            if total >= machine[selection]["cost"]:
                coffee -= machine[selection]["coffee"]
                milk -= machine[selection]["milk"]
                water -= machine[selection]["water"]
                print(f"Transaction completed. Your change is {total-machine[selection]['cost']}")
            else:
                print("Insufficient Funds! Try Again Later. Refunding all your coins")
        else:
            print("Insufficient Materials! Refill material. Try Again!")
        

