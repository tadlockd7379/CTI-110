# CTI 110
# P1HW2
# Drew Tadlock
# 11/3

def main():
    budget = number_input('What\'s your total budget? ')
    destination = input('Where do you want to travel? ') 
    gas = number_input('How much are you spending on gas? ')
    accomodations = number_input('How much are you spending on accomodations? ')
    food = number_input('How much are you spending on food? ')

    expenses = gas + accomodations + food
    result = budget - expenses

    print(f'\nDestination: {destination}')
    print(f'Total Budget: ${budget}\n')
    print(f'Gas: ${gas}')
    print(f'Accomdations: ${accomodations}')
    print(f'Food: ${food}\n')
    print(f'Remaining Balance: ${result}\n')

    main()

def number_input(ask):
    result = input(ask)
    try:
        result = int(result)
    except:
        print('Invalid number.')
        number_input(ask)
    return result

main()