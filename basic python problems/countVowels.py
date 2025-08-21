def count_vowels(str):
    count=0
    
    for i in str:
        if i in [ 'a', 'e', 'i', 'o', 'u' ]:
            count += 1

    return count


str = 'I will find you, and I will kill you!!!'
result = count_vowels(str.lower())
print(result)