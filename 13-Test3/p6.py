class C:
    def __init__(self,initial_value):
        self.counter = initial_value

    def m1(self):
        return self.counter
    
    def m2(self):
        self.counter += 1

    def m3(self):
        self.counter -= 1

    def m4(self, number):
        self.counter += number

