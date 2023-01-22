class Contact:
    def __init__(self,name,email,telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def show(self):
        print(self.name + " " + self.email + " " + self.telephone)

