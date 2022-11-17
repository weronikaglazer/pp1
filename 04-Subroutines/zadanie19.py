def check(number, x, y):
    if number > x and number <= y:
        return True
    if number == x:
        return True
    else:
        return False

print(check(4, 2, 6))
