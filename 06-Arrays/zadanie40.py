array  = [
    [-38,19],
    [5,40],
    [-7,11],
    [29,16]
]

min = float("inf")
max = float("-inf")

smallest_row = 0
smallest_col = 0
biggest_row = 0
biggest_col = 0


for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] < min:
            min = array[i][j]
            smallest_row = i + 1
            smallest_col = j + 1

        elif array[i][j] > max:
            max = array[i][j]
            biggest_row = i + 1
            biggest_col = j + 1

print(f"Smallest number is {min} and it's in row nr {smallest_row} and column nr {smallest_col}.")

print(f"Biggest number is {max} and it's in row nr {biggest_row} and column nr {biggest_col}.")
