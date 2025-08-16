def ispalindrome(string):
    org  = string.replace(' ', '').lower()
    reversed = ''
    
    for char in org[-1::-1]:
        reversed+=char

    return org == reversed

word = 'Ma dam'
result = ispalindrome(word)
print(result)