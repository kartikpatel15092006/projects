def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: Dividing by zero is not possible'

print('Kartik\'s First Project')
print('Simple Calculator')
print('Select operation:')
print('[1] Addition (+)')
print('[2] Subtraction (-)')
print('[3] Multiplication (*)')
print('[4] Division (/)')

choice = input('Enter choice [1/2/3/4]: ')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

if choice == '1':
    print('RESULT:', add(num1, num2))
elif choice == '2':
    print('RESULT:', subtract(num1, num2))
elif choice == '3':
    print('RESULT:', multiply(num1, num2))
elif choice == '4':
    print('RESULT:', divide(num1, num2))
else:
    print('Invalid input. Please select a valid operation.')
