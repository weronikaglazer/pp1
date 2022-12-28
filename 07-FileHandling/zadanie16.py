with open("sample3.txt", "r") as file_to_copy:
    with open("copy.txt", "w") as copy:
        content = file_to_copy.read()
        copy.write(content)