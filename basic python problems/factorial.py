def calc_factorial(num):
    factorial = 1
    
    while num > 0:
        factorial*= num
        num -= 1

    return factorial

num = 3
result = calc_factorial(num)
print(result)