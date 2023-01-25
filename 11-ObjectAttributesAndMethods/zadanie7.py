class Student():
    university = "UEK Krakow"
    last_id = 100000

    def __init__(self,name,surname,field):
        self.name = name
        self.surname = surname
        self.field = field
        Student.last_id += 1
        self.album_id = Student.last_id

    def __str__(self):
        return f"{self.name} {self.surname.upper()} ({str(self.album_id)}), {self.field},{Student.university}"
    

student1 = Student("Anna","Maj","Applied Informatics")
student2 = Student("Tim","Smith","Economics")
student3 = Student("Caroline","Gonzalez","Logistics")

print(student1)
print(student2)
print(student3)
