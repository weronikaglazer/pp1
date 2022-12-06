array = [1,3,5,6,7,3,2,5,9,4,6,8]
odd = []
even = []

for i in array:
    if (i not in even and i % 2 == 0):
        even.append(i)
    elif (i not in odd and i % 2 != 0):
        odd.append(i)

odd.sort()
even.sort()
new_array = []
for e in even:
    new_array.append(e)

for o in odd:
    new_array.append(o)




print(new_array)