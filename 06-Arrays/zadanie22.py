array1 = [4,36,12,28,9,44,5]
array2 = [5,1,36]


for i in range(0, len(array1)):
    if array2.__contains__(array1[i]):
        pass
    else:
        print(array1[i])
