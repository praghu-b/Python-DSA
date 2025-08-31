def missing_num(nums, n):
    res1 = 0
    res2 = 0

    for i in range(len(nums)):
        res2 = res2^nums[i]
        res1 = res1^(i+1)

    return res2^res1^n


nums = [2,3,4,5,6,7]
n = 7
print(missing_num(nums, n))