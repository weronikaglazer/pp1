array = [[3,9,3],[2,4,5],[7,1,6],[0,4,8]]

sum_even = 0
for row in array:
    for number in row:
        if number % 2 == 0:
            sum_even += number

print(sum_even)
