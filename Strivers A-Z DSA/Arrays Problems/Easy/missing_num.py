def missing_num(nums, n):
    res1 = 0
    res2 = 0

    for i in range(1,n+1):
        res1 ^= i

    for num in nums:
        res2 ^= num

    return res1^res2


nums = [1,2,3,4,5,7]
n = 7
print(missing_num(nums, n))