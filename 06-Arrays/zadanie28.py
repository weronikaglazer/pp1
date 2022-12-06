def median(array):
    array.sort()
    print(array)
    if (len(array) % 2 == 1):
        return array[int(len(array) / 2)]
    else:
        second = array[int(len(array) / 2)]
        first = array[int(len(array) / 2) - 1]
        return (second + first) / 2

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))