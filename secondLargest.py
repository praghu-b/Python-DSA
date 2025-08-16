def second_largest(nums):
    first_largest = nums[0]
    second_largest = 0

    for i in nums:
        if i > first_largest:
            second_largest = first_largest
            first_largest = i
        elif i > second_largest:
            second_largest = i

    return second_largest

nums = [42, 17, 89, 5, 73, 28, 91, 12, 65, 3, 58, 20, 77, 99, 34, 8, 51, 6, 95, 25]
result = second_largest(nums)
print(result)