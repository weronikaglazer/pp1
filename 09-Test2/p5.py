import re

def f(first_letter,last_letter):
    with open("data.txt", "r") as file:
        lines = file.readlines()
        counter = 0
        for line in lines:
            matches = re.findall(f"^{first_letter}\w*{last_letter}$", line) 
            if len(matches) != 0:
                counter += len(matches)
            else:
                continue
            
        
        return counter


