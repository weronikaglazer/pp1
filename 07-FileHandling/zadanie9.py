file = open('numbers.txt', 'r')

sum = 0

for number in file:
    sum += int(number)

file.close()

print(sum)


