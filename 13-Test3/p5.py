class C:
    def __init__(self,array):
        self.array = array

    def __str__(self):
        total = sum(self.array)
        string = ""
        self.array = [str(number) for number in self.array]
        string += "+".join(self.array)
        string += "=" + str(total)
        return string
    


