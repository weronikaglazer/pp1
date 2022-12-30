import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"

temperatures = re.findall("\d{2}",message)
temperatures_int = []

for temperature in temperatures:
    temperatures_int.append(int(temperature))

print(temperatures_int)

sum = sum(temperatures_int)
amount = len(temperatures_int)

average = sum / amount

print(f"The average tempreature is {average}C")