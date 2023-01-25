class C:
    def __init__(self,dictionary):
        self.students = dictionary

    def m(self,n):
        students = []
        for key,value in self.students.items():
            average = sum(value) / len(value)
            if (average >= n):
                students.append(key)
        students.sort()
        string = ",".join(students)
        return string
    
