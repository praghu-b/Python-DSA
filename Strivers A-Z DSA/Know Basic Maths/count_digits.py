def count_digit(num):
    string = str(num)
    length = len(string)-1 if num < 0 else len(string)
    return length


x = int(input('Number? '))
print(count_digit(x))