def sum_even(nums):
    total = 0
    for num in nums:
        if num%2 == 0:
            total+=num
    return

nums = [1, 2, 3, 4, 5, 6]
result = sum_even(nums)
print(result)