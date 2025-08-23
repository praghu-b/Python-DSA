def one_n(n):
    if n > 1:
        one_n(n-1)
        print(n)
    else:
        print(1)


one_n(int(input('Number? ')))