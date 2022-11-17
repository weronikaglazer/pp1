def digit_calc(number):
    string = str(number)
    sum = 0
    for digit in string:
        digit = int(digit)
        sum += digit
    return sum

print(digit_calc(7182))