# CTI 110
# P1HW2
# Drew Tadlock
# 11/3

def input_float(ask):
    result = input(ask)
    try:
        result = float(result)
    except:
        print('Invalid number.')
        input_float(ask)
    return result

budget = input_float('What\'s your total budget? ')
destination = input('Where do you want to travel? ') 
gas = input_float('How much are you spending on gas? ')
accomodations = input_float('How much are you spending on accomodations? ')
food = input_float('How much are you spending on food? ')

expenses = gas + accomodations + food
result = budget - expenses

print(f'\n---------- Travel Expenses ----------')
print(f'Destination:        {destination}')
print(f'Total Budget:       ${budget}')
print(f'Gas:                ${gas}')
print(f'Accomdations:       ${accomodations}')
print(f'Food:               ${food}')
print(f'-------------------------------------\n')
print(f'Remaining Balance:  ${result}')    