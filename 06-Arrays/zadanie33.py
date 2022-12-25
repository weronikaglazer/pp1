import random

array = [random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999),random.randint(1,999)]

divider = "------------------------------------"
print(divider)

for number in array:
    print(f"|{number:>3}", end="")
    
print("|")
print(divider)