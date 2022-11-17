def letter_counter(text, letter):
    count = 0
    for char in text:
        if char == letter:
            count += 1
    
    return count

print(letter_counter("You never get a second chance to make a first impression", "e"))