names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest = names[0]

for name in names:
    if names[name] > len(longest):
        longest = names[name]

print(longest)