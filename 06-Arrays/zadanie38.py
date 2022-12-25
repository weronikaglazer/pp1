def create_2d_arr(x,y):
    array = []

    for i in range(x):
        row = []
        for j in range(y):
            row.append(0)
        array.append(row)

    return array

print(create_2d_arr(3,5))