def reverse(x):
        org = x
        mod = abs(x)
        new = 0

        while mod > 0:
            digit = mod%10
            new = new*10 + digit
            mod = mod//10

        if -2**31 <= new > 2**31 - 1:
            pass
        else:
            return 0

        if org < 0:
              return -(new)

        return new


x = 120
print(reverse(x))