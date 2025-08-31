def find_once(nums):
    res = 0

    for num in nums:
        res^=num

    return res

nums = [1,1,2,2,3,3,4,4,5]
print(find_once(nums))
