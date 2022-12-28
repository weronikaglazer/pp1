with open("MeatAndFish.txt", "r") as meat:
    with open("GrainsAndBread.txt", "r") as bread:
        with open("shoppinglist.txt", "w") as list:
            for product in meat:
                list.write(product)
            list.write("\n")
            for product in bread:
                list.write(product)