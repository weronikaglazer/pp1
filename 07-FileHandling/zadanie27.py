with open("grades.txt", "r") as file:
    lines = file.readlines()
    name_line = lines[0]
    name_line_content = name_line.split(":")
    name = name_line_content[1].strip()

    grades_line = lines[1]
    
    grades_string = grades_line.replace("Grades: ", "")

    grades = grades_string.split(",")

    grades = [float(x) for x in grades]
    
    amount = len(grades)
    sum = sum(grades)

    average = round(sum / amount, 2)
    
    print(f"The average grade of {name} is: {average}")            
