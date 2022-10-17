# zadanie 18. 

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

area = (a + b + c) / 2

print(area)

# zadanie 19.

height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100) ** 2
print(f"Your BMI is {bmi}")


# zadanie 20.
import random

roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)
roll3 = random.randint(1, 6)

print(roll1, roll2, roll3)

sum = roll1 + roll2 + roll3

print(sum)