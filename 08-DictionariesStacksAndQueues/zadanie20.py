import stack

def convert_to_binary(number):
    if number == 0:
        return 0

    while number > 0:
        remainder = number % 2
        stack.push(remainder)
        number = number // 2

    converted_number = ""
    while stack.empty() == False:
        converted_number += str(stack.pop())

    return converted_number


