array = [[True, False],[True,True],[False,False]]

for row in range(0,len(array)):
    for value in range(0,len(array[row])):
        if (array[row][value]):
            array[row][value] = False
        else:
            array[row][value] = True


print(array)

