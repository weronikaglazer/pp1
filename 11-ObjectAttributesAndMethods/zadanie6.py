# class definition
class Film():         
    cinema = "Multikino"    

    def __init__(self, title):        
        self.title = title 

    def __str__(self):        
        return f"{self.title} ({Film.cinema})"    

film1 = Film("The Shawshank Redemption")
print(film1)
film2 = Film("Pulp Fiction")
print(film2)

Film.cinema = "Cinema City"
print(film1)
print(film2)