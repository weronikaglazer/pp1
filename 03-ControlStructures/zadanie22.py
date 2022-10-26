# Write a program that displays numbers from 1 to 30. If the number is divisible by 3 then the program displays the word 'THREE'. Next, if the number is divisible by 5 then the program displays the word 'FIVE'. Finally, if the number is divisible by both 3 and 5 then the program displays the word 'BINGO'. 

def display_numbers():
    for i in range(1,31):
        if (i % 5 == 0 and i % 3 == 0):
            print("BINGO")
        elif (i % 5 == 0):
            print("FIVE")
        elif (i % 3 == 0):
            print("THREE")
        else:
            print(i)

display_numbers()