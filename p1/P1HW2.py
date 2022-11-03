# CTI 110
# P1HW2
# Drew Tadlock
# 11/3

def input_int(ask):
    result = input(ask)
    try:
        result = int(result)
    except:
        print('Invalid number.')
        input_int(ask)
    return result

budget = input_int('What\'s your total budget? ')
destination = input('Where do you want to travel? ') 
gas = input_int('How much are you spending on gas? ')
accomodations = input_int('How much are you spending on accomodations? ')
food = input_int('How much are you spending on food? ')

expenses = gas + accomodations + food
result = budget - expenses

print(f'\nDestination: {destination}')
print(f'Total Budget: ${budget}\n')
print(f'Gas: ${gas}')
print(f'Accomdations: ${accomodations}')
print(f'Food: ${food}\n')
print(f'Remaining Balance: ${result}\n')