array = [12, 6, 4, 9, 10]

def star(array):
    for i in range(0, len(array)):
        starr = "*"
        print(f"{array[i]}: {array[i]*starr}")
    
star(array)
