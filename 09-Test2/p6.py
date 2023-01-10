import json

def f(age,course,average):
    with open("data.json","r") as file:
        data_array = json.load(file)
        counter = 0
        for student in data_array:
            if student.get("age") >= age:
                studies_dict = student["studies"]
                courses_array = studies_dict["courses"]
                for item in courses_array:
                    if item.get("name") == course:
                        grades_sum = 0
                        for grade in item.get("grades"):
                            grades_sum += grade
                        average_grade = grades_sum / len(item.get("grades"))
                        if average_grade >= average:
                            counter += 1
                        else:
                            continue
                    else:
                        continue
        return counter





