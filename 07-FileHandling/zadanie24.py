import re

text = "To be, or not to be, that is the question"

vowels = re.findall("[aoeui]", text)

number = len(vowels)
print(f"The number of vowels in the text is {number}")