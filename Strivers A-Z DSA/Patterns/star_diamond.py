def start_diamond(num):
    for i in range(num):
        j = 0
        while j < num-i-1:
            print(' ', end=' ')
            j += 1
        j = 0
        while j < i*2+1:
            print('*', end=' ')
            j += 1
        j = 0
        while j < num-i-1:
            print(' ', end=' ')
            j += 1
        print()

    for i in range(num):
        j = 0
        while j < i:
            print(' ', end=' ')
            j += 1
        j = 0
        while j < 2*num - (2*i + 1) :
            print('*', end=' ')
            j += 1
        j = 0
        while j < i:
            print(' ', end=' ')
            j += 1
        print()


start_diamond(int(input('Number? ')))