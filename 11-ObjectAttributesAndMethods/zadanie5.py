class Song():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album_title = album
        self.release_year = year

    def __str__(self):
        return "Performer: " + self.artist + "\n" + "Song: " + self.title + "\n" + "Album: " + self.album_title + "\n" + "Year: " + self.release_year + "\n"
    
song1 = Song("Ed Sheeran", "Supermarket Flowers", "Divide", "2017")
print(song1)