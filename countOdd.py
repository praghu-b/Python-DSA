def count_odd(nums):
    count = 0

    for num in nums:
        if num%2 != 0:
            count+=1

    return count

nums = [ 1, 2, 3, 4, 5, 6 ]
result = count_odd(nums)
print(result)