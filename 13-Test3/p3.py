import re

def f1(t):
    family = {}
    names = []
    ages = []
    words = t.split()
    for word in words:
        word = re.sub(r'[!,.]','',word)
        if word.istitle():
            names.append(word)
        elif word.isdigit():
            ages.append(word)
        
    for i in range(len(names)):
        family[names[i]] = ages[i]

    sorted_names = sorted(family.keys())
    sorted_family = {name: family[name] for name in sorted_names}
    return sorted_family


def f2(d):
    total = 0
    for value in d.values():
        total += int(value)
    
    return total

