arr = [-15, 8, -31, 47, -2, 19]

min = arr[0]
max = arr[0]

for i in range(1, len(arr)):
    if  arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

    
        
    
print(f"max= {max}, min= {min}")