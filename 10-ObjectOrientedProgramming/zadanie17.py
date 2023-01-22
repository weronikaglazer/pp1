class Statistics():
    def __init__(self):
        self.set = []

    def add(self):
        self.set.append(int(input("Enter the number: ")))
    
    def display(self):
        new_set = []
        for number in self.set:
            new_set.append(str(number))
        print(" ".join(new_set))

    def greatest(self):
        print("The greatest number is " + str(max(self.set)))

    def smallest(self):
        print("The smallest number is " + str(min(self.set)))

    def arithmetic_mean(self):
        result = sum(self.set) / len(self.set)
        print("The arithmetic mean of the set is " + str(result))

    def median(self):
        self.set.sort()
        if (len(self.set) % 2 == 0):
            print("The median is " + str(self.set[len(self.set)/2]))
        else:
            median = self.set[len(self.set)//2] + self.set[(len(self.set)//2) + 1] / 2
            print("The median is " + str(median))

    def show_statistics(self):
        self.greatest()
        self.smallest()
        self.arithmetic_mean()
        self.median()

set1 = Statistics()
set1.add()
set1.display()
set1.add()
set1.add()
set1.add()
set1.add()
set1.display()
set1.show_statistics()