def gcd(num1, num2):
    
    for i in range(min(num1, num2), 0, -1):
        if num1%2 == 0 and num2%2 == 0:
            return i
    
    return 1
    

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
result = gcd(num1, num2)
print(result)