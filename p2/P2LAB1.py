# CTI 110
# P2LAB1 - Driving Costs
# Drew Tadlock
# 11/8

# Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input
# output the gas cost for 20 miles, 75 miles, and 500 miles.
# in other words, find the cost to drive 1 mile, then multiply

# Cost per mile is:
# cost per gallon, divided by miles per gallon

def input_float(ask):
    result = input(ask)
    try:
        result = float(result)
    except:
        print('Invalid number.')
        input_float(ask)
    return result

def cost(miles):
    return miles * cost_per_mile

print('This program determines cost of a car trip.')

miles_per_gallon = input_float('How many miles can you travel with one gallon of gas? ')
cost_per_gallon = input_float('How much does a gallon of gas cost? ')
cost_per_mile = cost_per_gallon / miles_per_gallon

print(f'It costs ${cost_per_mile:.2f} to travel one mile.')
print(f'20 miles: ${cost(20):.2f}')
print(f'75 miles: ${cost(75):.2f}')
print(f'500 miles: ${cost(500):.2f}')
