def convert_to_1d(array):
    converted = []

    for row in array:
        for element in row:
            converted.append(element)

    return converted

array1 = [
    [2,3],
    [1,5]
]

array2 = [
    [5,0,3,7,5],
    [9,0,9,1,2]
]

array3 = [
    [2,1],
    [3,5],
    [7,4],
    [2,6]
]

print(convert_to_1d(array1))
print(convert_to_1d(array2))
print(convert_to_1d(array3))