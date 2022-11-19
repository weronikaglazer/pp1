arr = [1, 2, 3, 4, 5]

arr[0] -= 1
arr[-1] += 4
arr[len(arr) // 2] *= 2

for i in range(len(arr)):
    arr[i] += 3

print(arr)