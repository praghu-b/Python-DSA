def half_diamond(num):

    for i in range(num*2):
        if i < num:
            stars = i+1
        elif i >= num:
            stars = num*2 - i - 1

        for j in range(stars):
            print('*', end=' ')

        print()



half_diamond(int(input('Number? ')))

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *