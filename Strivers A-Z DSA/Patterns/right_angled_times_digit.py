def func(num):
    for i in range(num):
        for j in range(i+1):
            print(i+1, end='')
        print()

func(int(input('Number? ')))