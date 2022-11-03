# CTI 110
# P1Lab1 - Apple Salesman
# Drew Tadlock
# 10/25

# This program pretends to sell apples.
"""
The salesperson's name is Drew, and they have 100 apples for sale.
Our goal is to write a program which displays the saleperson's store name,
price per apple, and the price to purchase them all at once
"""

import random

name = 'Drew'
print(f'Welcome to {name}\'s apple stand.')

apples = 100
price = 0.25

print(f'There are {apples} apples for sale for ${price} each.')

print(f'You can buy individual apples or buy all {apples} for ${price * 100}')

money = random.randint(1, 30)

print(f'You have ${money} to spend on apples. You can buy {money/price} apples with this money.')

def purchase():
    global apples, price, money
    
    try:
        amount = int(input('How many apples do you want to buy? '))
    except:
        print('Invalid amount.')
        purchase()

    if apples < amount:
        print('The shop doesn\'t have enough apples.')
        purchase()
    else:
        cost = price * amount
        if money < cost:
            print(f'You need ${cost - money} more to buy {amount} apples.')
            purchase()
        else:
            money -= cost
            apples -= amount
            if apples == 0:
                print(f'You purchased all of the shop\'s apples! You have ${money} left.')
                exit()
            else:
                print(f'You purchased {amount} apples for ${cost}. You now have ${money} left and the shop has {apples} apples left.')
                if money == 0:
                    print('You spent all of your money.')
                    exit()
                else:
                    print(f'You have ${money} to spend on apples. You can buy {money/price} apples with this money.')
            purchase()
        
purchase()