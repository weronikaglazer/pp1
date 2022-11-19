arr = [[2,5,4],[9,0,3]]

print(arr)
print(len(arr))
print(len(arr[0]))
print(arr[0][1])
print(arr[1][2])

for i in arr[1]:
    print(i, end=" ")
print()

for y in arr:
    for x in y:
        print(x, end=" ")
    print()

for y in arr:
    print(y[2])