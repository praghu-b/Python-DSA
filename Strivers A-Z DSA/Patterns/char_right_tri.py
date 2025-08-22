def char_right_tri(num):
    for i in range(num):
        for j in range(65, 65+i+1):
            print(chr(j), end=' ')
        print()

char_right_tri(int(input('Number? ')))