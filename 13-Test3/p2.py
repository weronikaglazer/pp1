def f(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != (i+1)*(j+1):
                return False
    
    return True

