# 16.	Write a program that displays two numbers entered from the keyboard in ascending order.

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))

if x > y:
    print(f'Numbers in ascending order: {y}, {x}')
else:
    print(f'Numbers in ascending order: {x}, {y}')