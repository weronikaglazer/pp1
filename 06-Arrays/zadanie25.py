def occurs(number, array):
    if array.__contains__(number):
        return True
    else:
        return False

array = [15, 38, 7, 23, 14]
user_input = int(input("Enter the number: "))
print(occurs(user_input, array))