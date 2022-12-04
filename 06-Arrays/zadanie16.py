array = [15,8,31,47,2,19]

reversed_array = []

for i in range(len(array)-1, -1, -1):
    reversed_array.append(array[i])

print(f"existed array: {array}")
print(f"reverse array: {reversed_array}")
