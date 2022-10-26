# 18.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

start_amount = int(input("Enter the amount you want to count: "))

amount = start_amount

five_zlotych_coins = 0
two_zlotych_coins = 0
one_zlotych_coins = 0

if (amount >= 5):
    amount //= 5
    five_zlotych_coins = amount
    amount = start_amount - five_zlotych_coins * 5
    start_amount = amount

if (amount >= 2):
    amount //= 2
    two_zlotych_coins = amount
    amount = start_amount - two_zlotych_coins * 2
    start_amount = amount

if (amount >= 1):
    one_zlotych_coins = amount

print("The amount of {0} in coins is: \n 5 zl: {1} \n 2 zl: {2} \n 1 zl: {3}" .format(amount, five_zlotych_coins, two_zlotych_coins, one_zlotych_coins))