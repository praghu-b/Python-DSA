def gcd(num1, num2):
    num1_divs = set()
    num2_divs = set()
    gcd = 0
    
    for i in range(1, min(num1, num2)+1):
        if num1%i == 0:
            num1_divs.add(i)
            if i in num2_divs and i > gcd:
                gcd = i
        if num2%i == 0:
            num2_divs.add(i)
            if i in num1_divs and i > gcd:
                gcd = i

    return gcd
    

num1 = int(input('Num1: '))
num2 = int(input('Num2: '))
result = gcd(num1, num2)
print(result)