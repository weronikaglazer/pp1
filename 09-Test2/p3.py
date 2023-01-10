def f(array2D):
    sums = []

    for i in range(len(array2D[0])):
        column_sum = 0
        for row in array2D:
            column_sum += row[i]
        sums.append(column_sum)

    return sums


