def count_characters(str):
    characters = {}
    str = str.replace(' ', '').lower()
    
    for char in str:
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] = characters[char] + 1

    return characters

name = 'Madam'
result = count_characters(name)
print(result)