import json

student = {
    "name": "Felice",
    "age": 18,
    "nationality": "Spanish",
    "favorite subject": "art",
    "passed": True,
    "average grade": 4.02,
    "friends": ["Bailey", "Matt", "Sophie", "Delilah"],
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=2)