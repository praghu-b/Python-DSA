def rotate_list(nums, k):
    result = []
    remainder = k % len(nums)

    for num in nums[-remainder:]:
        result.append(num)

    for num in nums[:-remainder]:
        result.append(num)

    return result


nums = [10, 20, 30, 40, 50, 60]
k = 3
result = rotate_list(nums, k)
print(result)