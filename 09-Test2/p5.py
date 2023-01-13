def f(first_letter,last_letter):
    with open("data.txt", "r") as file:
        counter = 0
        for line in file:
            words = line.strip().split()
            for word in words:
                if word.startswith(first_letter) and word.endswith(last_letter):
                    counter += 1
        return counter

print(f('w','d'))



