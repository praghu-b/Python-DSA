def largest_in_list(nums):
    largest = nums[0]

    for i in nums:
        largest = i if i > largest else largest

    return largest

nums = [2,3343423423,343,2,423,22324,2321]
result = largest_in_list(nums)
print(result)