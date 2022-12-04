array = [[0,0,0],[0,0,0],[0,0,0]]

x = 0

for i in range(0, len(array)):
    array[i][x] = 1
    x += 1
    for j in array[i]:
        print(j, end=" ")
    print()