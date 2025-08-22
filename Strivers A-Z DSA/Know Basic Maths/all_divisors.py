def all_divisors(num):
    i = 1
    while i <= num:
        if num%i == 0:
            print(i, end=' ')
        i+=1
        

num = int(input('Number? '))
all_divisors(num)