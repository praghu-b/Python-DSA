def char_hashing(string, chars):
    chars_map = dict.fromkeys(chars, 0)
    
    for c in string:
        if c in chars_map:
            chars_map[c] += 1

    return chars_map

string = 'prakash'
chars = [ 'a', 'b', 'c', 'd', 'e' ]
print(char_hashing(string, chars))