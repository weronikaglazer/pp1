import random

with open("random_numbers.txt", "w") as file:
    for i in range(1,51):
        random_number = random.randint(100,999)
        file.write(str(random_number) + "\n")