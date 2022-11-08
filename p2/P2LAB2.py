# CTI 110
# P2LAB2 - Food Receipt Pt 1
# Drew Tadlock
# 11/8

def input_float(ask):
    result = input(ask)
    try:
        result = float(result)
    except:
        print('Invalid number.')
        input_float(ask)
    return result

def ask_item():
    food = input('Enter food item name: ')
    price = input_float('Enter item price: ')
    quantity = input_float('Enter item quantity: ')
    return { 'food': food, 'price': price, 'quantity': quantity }

items = []

# change the number in range() to ask for a different amount of items
for _ in range(2):
    items.append(ask_item())

total = 0

print(f'\nRECEIPT:\n')
for i in items:
    print(f'{i.get("quantity")} {i.get("food")} @ ${i.get("price"):.2f} each = ${i.get("quantity") * i.get("price"):.2f} total')
    total += i.get('price')

tip = total * .15
print(f'\nTotal Cost: ${total:.2f}\n15% tip: ${tip:.2f}\nTotal with tip: ${total + tip:.2f}\n')