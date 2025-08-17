def count_characters(str):
    characters = {}
    str = str.replace(' ', '').lower()
    
    for char in str:
        characters[char] = characters.get(char, 0) + 1

    return characters

name = 'Madam'
result = count_characters(name)
print(result)