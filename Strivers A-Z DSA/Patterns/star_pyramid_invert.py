def star_pyramid(num):
    for i in range(num):
        j = 0
        while j < i:
            print(' ', end='')
            j+=1
        
        j = 0
        while j < 2*num - (2*i + 1):
            print('*', end='')
            j+=1

        j = 0
        while j < i:
            print(' ', end='')
            j+=1

        print()



star_pyramid(int(input('Number? ')))