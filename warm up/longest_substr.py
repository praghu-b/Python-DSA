# find the length of the longest substring without repeating characters

def longest_substr(str):
    if len(str) == 0:
        return 0
    
    seen = {}
    max_count = 0
    count = 0
    
    i = 0
    
    while i < len(str):
        if str[i] not in seen:
            count += 1
            seen[str[i]] = i
            i += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
            i = seen[str[i]]+1
            seen.clear()
            
    return max_count
    

str = 'ab'
print(longest_substr(str))