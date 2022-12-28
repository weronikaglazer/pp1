with open("sample3.txt", "r") as file:
    lines = file.readlines()
    for line in lines[:5]:
        print(line)
        