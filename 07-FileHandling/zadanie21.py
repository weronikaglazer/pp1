with open("powered-numbers.txt", "w") as file:
    for i in range(1,11):
        line = str(i) + ", " + str(i**2) + ", " + str(i**3) + "\n"
        file.write(line)
        