def is_anagram(str1, str2):
    seen = dict()

    if len(str1) != len(str2):
        return False

    for s in str1:
        if s in seen:
            seen[s] += 1
        else:
            seen.update({s:1})

    for s in str2:
        if s in seen and seen[s] > 0:
            seen[s] -= 1
            print(seen)
        else:
            return False
    
    return True


str1, str2 = 'sadder', 'dreads'
result = is_anagram(str1, str2)
print(result)