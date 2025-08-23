total = 1

def factorial(n):
    global total
    if n == 1:
        print(total)
        return
    total *= n
    factorial(n-1)


num = int(input('Number? '))
factorial(num)