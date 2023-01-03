import json

with open("students.json", "r") as initial_file:
    data = json.load(initial_file)
    for student in data:
        limited_student = {key: student[key]for key in ["name", "surname", "student ID"]}
        with open("limited.json", "a") as file:
            json.dump(limited_student, file, indent=2)
