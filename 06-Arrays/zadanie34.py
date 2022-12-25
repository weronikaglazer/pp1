array1 = [3,8,6,4]
array2 = [1,3,4,5,7,8,6,3,5,4]


def check_if_subset(first_arr, second_arr):
    is_subset = True
    for number in first_arr:
        if number not in second_arr:
            is_subset = False
        
    return is_subset


print(check_if_subset(array1,array2))