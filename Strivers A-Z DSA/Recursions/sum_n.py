sum = 0
def sum_of_n(n):
    global sum
    if n == 0:
        print(sum)
        return
    sum += n
    sum_of_n(n-1)
    
    

n = int(input('Number? '))
sum_of_n(n)