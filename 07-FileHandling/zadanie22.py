import csv

with open("students.csv", "r") as file:
    reader = csv.reader("students.csv")
    next(reader)

    for row in reader:
        age = int(row[2])

        if age < 30:
            print(f"{row[0]} {row[1]}: {row[2]}")





