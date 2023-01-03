import json

book = {
    "title": "Where the Crawdads Sing",
    "author": "Delia Owens",
    "published in": 2018,
    "genre": "mystery",
    "pages": 416,
    "translated": True,
    "characters": ["Kya", "Tate", "Chase", "Jumpin'"]
}

with open("favourite.json", "w") as file:
    json.dump(book, file, indent=2)

