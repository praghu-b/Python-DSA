def func(num):
    col= num
    for i in range(num):
        for j in range(col):
            print(j+1, end='')
        col-=1
        print()
            

func(int(input('Number? ')))