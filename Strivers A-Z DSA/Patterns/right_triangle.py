def right_triangle(num):
    for i in range(num):
        for j in range(i+1):
            print('*', end='')
        print()


num = int(input('Enter input: '))
right_triangle(num)