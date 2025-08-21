def rectangular(num):
    for i in range(num):
        for j in range(num):
            print('*', end='')
        print()

num = int(input('Enter a number: '))
rectangular(num)