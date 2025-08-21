def reverse_string(str):
    reverse = ''
    i = len(str)-1
    j = 0

    while(i >= 0 and j < len(str)):
        reverse += str[i]
        i-=1
        j+=1

    return reverse

str = 'Prakash'
result = reverse_string(str)
print(result)