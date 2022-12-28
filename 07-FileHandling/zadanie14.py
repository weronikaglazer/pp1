file_name = input("Enter the file name: ")

with open(file_name, "r") as file:
    counter = 0
    for line in file:
        counter += 1

print(f"File name: {file_name}")
print(f"Number of lines: {counter}")