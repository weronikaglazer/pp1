with open("sample3.txt", "r") as file_to_copy:
    with open("copy.txt", "w") as copy:
        for line in file_to_copy:
            copy.write(line)