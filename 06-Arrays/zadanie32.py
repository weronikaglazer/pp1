def array_to_string(array):
    converted_list = [str(element) for element in array]
    string = ",".join(converted_list)
    return string


print(array_to_string([1,2,3,4,5,6,7]))