def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for i in range(len(str1)):
        freq1[str1[i]] = freq1.get(str1[i], 0) + 1
        freq2[str2[i]] = freq2.get(str2[i], 0) + 1
            
    return freq1 == freq2


str1 = 'anagram'
str2 = 'nagaram'
print(is_anagram("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"))