array = [5,1,9,6,1]
array1 = []

array1 += array

largest = max(array)

array.remove(largest)

second_largest = max(array)

print(f"Array: {array1}")
print(f"Result: {second_largest}")