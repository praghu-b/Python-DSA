def right_angled_num(num):
    for i in range(num):
        count = 1
        for j in range(i+1):
            print(count, end='')
            count+=1
        print()
    

num = int(input('Enter input: '))
right_angled_num(num)