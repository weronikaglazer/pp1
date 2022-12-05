array = [2,3,2,5,8,1,9,8]
uniques = []
for i in array:
    if (array.count(i)==1):
        uniques.append(i)

print(f"Array: {array}")
print(f"Unique elements: {uniques}")