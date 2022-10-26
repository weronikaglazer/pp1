# Write a program that calculates a dog's age in dog’s years. For the first two years, a dog's life is equal to 10.5 human years. After that, each dog year is equal to 4 human years. 

dog_human_age = int(input("Enter your dog's human age: "))

if (dog_human_age == 2):
    print("Your dog's age in dog years is 10.5 years")

if (dog_human_age < 2):
    baby_age = int(dog_human_age * 5.25)
    print("Your dog's age in dog years is {0} years" .format(baby_age))

if (dog_human_age > 2):
    age_to_convert = dog_human_age - 2
    dog_age =  age_to_convert * 4 + 10.5
    print("Your dog's age in dog years is {0} years" .format(dog_age))


