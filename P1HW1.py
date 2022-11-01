# CTI 110
# P1HW1
# Simple Input Output

def main():
    num = input('Please enter a number: ')
    try:
        num = int(num)
    except:
        print('Invalid number.')
        main()

    print(f'You chose {num}')
    print(f'{num} squared is {num * num}')
    print(f'{num} + 5 is {num + 5}')
    print(f'{num} * 5 is {num * 5}')

main()