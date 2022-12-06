def minmax(array):
    largest = max(array)
    smallest = min(array)
    new_array = []
    new_array.append(smallest)
    new_array.append(largest)

    return new_array

print(minmax([4,2,8,4,7,9,5]))


    
