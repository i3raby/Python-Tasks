def Start() :
    print('Select operation')
    print('————————————————')
    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')

    choice = input('\nEnter choice → ')

    if choice in ['1', '2', '3', '4'] :
        try:
            N1 = float(input('Enter First Number → '))
            N2 = float(input('Enter Second Number → '))
        except ValueError:
            print('Invalid input! Please enter numeric values.')
            return

        if choice == '1':
            print(f"The result is: {add(N1, N2)}")
        elif choice == '2':
            print(f"The result is: {subtract(N1, N2)}")
        elif choice == '3':
            print(f"The result is: {multiply(N1, N2)}")
        elif choice == '4':
            print(f"The result is: {divide(N1, N2)}")
    else:
        print('Invalid input! Please select a valid operation.')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return 'Error: Division by zero is not allowed.'

Start()