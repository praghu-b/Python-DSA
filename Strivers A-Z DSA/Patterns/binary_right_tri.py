def binary_right_tri(num):
    for i in range(num):
        no = 0 if (i+1)%2 == 0 else 1
        for j in range(i+1):
            print(no, end=' ')
            no = 0 if no == 1 else 1
        print()


binary_right_tri(int(input('Number?')))