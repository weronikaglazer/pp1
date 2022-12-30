import re

with open("sample3.txt", "r") as file:
    lines = file.readlines()
    
    for line in lines:
        words = re.findall("\w{6}\w*", line)
        for i in words:
            print(i)
        
