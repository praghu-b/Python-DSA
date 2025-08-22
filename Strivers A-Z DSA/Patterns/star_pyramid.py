def star_pyramid(num):
    for i in range(num):
        j = 0
        while j < num-i-1:
            print(' ', end='')
            j+=1
        
        j = 0
        while j < i*2+1:
            print('*', end='')
            j+=1

        j = 0
        while j < num-i-1:
            print(' ', end='')
            j+=1

        print()


star_pyramid(int(input('Number? ')))