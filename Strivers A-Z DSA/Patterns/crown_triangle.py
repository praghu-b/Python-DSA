def crown_triangle(num):
    spaces = 2*(num - 1)

    for i in range(num):
        for j in range(i+1):
            print(j+1, end=' ')
        for j in range(spaces):
            print(' ', end=' ')
        for j in range(i+1):
            print(i+1-j, end=' ')

        print()
            
        spaces-=2


crown_triangle(int(input('Number? ')))