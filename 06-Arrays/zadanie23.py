def bubblesort(array):
    swapped = False
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if (array[j]>array[j+1]):
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            pass
    return array
array = [1,6,7,3,4,5,9,2]
array2 = [4,7,3,2]
print(bubblesort(array))
print(bubblesort(array2))