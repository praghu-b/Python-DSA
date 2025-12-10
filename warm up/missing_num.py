def find_missing_num(nums):
    n = len(nums)
    formula = n*(n+1)//2
    sum = 0

    for num in nums:
        sum+=num

    return formula-sum

nums = [1, 0, 3, 5, 2]
print(find_missing_num(nums))