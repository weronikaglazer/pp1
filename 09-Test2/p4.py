def f(dictionary,x,y):
    sum = 0

    for array in dictionary.values():
        for value in array:
            if value >= x and value <= y:
                sum += value
            else:
                continue
        
    return sum

        