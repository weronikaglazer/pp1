class Phone():
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
        self.is_on = False

    def __str__(self):
        return self.color + " " + self.brand
    
    def switch(self):
        self.is_on = not self.is_on
        if self.is_on:
            print("Phone is on")
        else:
            print("Phone is off")

    def call(self,person):
        print("Calling " + person + ".....")


phone1 = Phone("iPhone 12","black")
phone2 = Phone("Samsung Galaxy", "white")
print(phone1)
print(phone2)
phone1.switch()
phone2.switch()
phone1.call("David")