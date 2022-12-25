array = [
    [2,5,4,3,6],
    [6,5,3,9,7],
    [5,4,1,3,8]
]

print("Before:")
for row in array:
    print(row)


for i in range(len(array[0])):
    array[0][i], array[-1][i] = array[-1][i], array[0][i]

print()
print("After:")

for row in array:
    print(row)

