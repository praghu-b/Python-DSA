def one_n(n):
    if n > 1:
                    #----<----|
        one_n(n-1)           #|     Move this line to print n to 1 using recursion
        print(n)    #---->----|
    else:
        print(1)


one_n(int(input('Number? ')))