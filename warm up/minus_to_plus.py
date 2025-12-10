def minus_to_plus(nums):
    neg_arr = []
    pos_arr = []

    for num in nums:
        if num < 0:
            neg_arr.append(num)
        else:
            pos_arr.append(num)

    return neg_arr+pos_arr

nums = [1, -2, 3, -4, -1, 5]
print(minus_to_plus(nums))