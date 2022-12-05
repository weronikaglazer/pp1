array = [15,8,31,47,2,19]
i = 0
sum = 0
arithmetic_mean = 0
length = len(array)

while i < len(array):
    sum += array[i]
    i+=1

arithmetic_mean = sum / length

print(array)
print(arithmetic_mean)
