product = input("What do you want to add? : ")
with open("shopping.txt", "a") as file:
    file.write(product + "\n")

