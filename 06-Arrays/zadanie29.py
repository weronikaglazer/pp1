array = [1,2,3,4,5,6,7]

user_input = int(input("Enter a number: "))
greater = 0
for i in array:
    if i > user_input:
        greater += 1


print(greater)
