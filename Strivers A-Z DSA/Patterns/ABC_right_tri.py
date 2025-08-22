def ABC_right_tri(num):
    
    char=65
    for i in range(num):
        for j in range(i+1):
            print(chr(char), end='')
        char+=1
        print()


ABC_right_tri(int(input('Number? ')))