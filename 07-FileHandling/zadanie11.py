film_titles = ["Twilight", "Toy Story", "Fight Club", "Titanic", "Shrek"]

file = open('movies.txt', 'w')

for movie in film_titles:
    file.write(movie + "\n")

file.close()