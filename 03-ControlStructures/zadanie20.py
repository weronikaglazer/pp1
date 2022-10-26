# Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user. 

user_number = int(input("Enter a number: "))

for i in range(1,11):
    print("{0} * {1} = {2}" .format(user_number, i, user_number * i))