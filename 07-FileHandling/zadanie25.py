import re

text = "To be, or not to be, that is the question"

words = re.split("\s", text)
print(len(words))