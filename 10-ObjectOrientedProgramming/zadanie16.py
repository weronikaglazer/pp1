import random
class Account():
    def __init__(self,number):
        self.number = number
        self.balance = 0

    def show_status(self):
        print("Bank Account No: " + self.number)
        print("Balance: " + "PLN " + str(round((float(self.balance)),2)))

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if (self.balance < amount):
            print("Insufficient funds on the account.")
        else:
            self.balance -= amount


account1 = Account("12 3456 5555 9090 1111 0000 7722")
account1.show_status()
account1.deposit(25.30)
account1.show_status()
account1.withdraw(31.70)
account1.show_status()
account1.withdraw(14)
account1.show_status()
