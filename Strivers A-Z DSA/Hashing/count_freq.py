def count_freq(nums):
    nums_map = dict.fromkeys(nums, 0)

    for i in nums:
        if i in nums_map:
            nums_map[i] += 1

    return nums_map


nums = [2,2,3,4,4,2]
print(count_freq(nums))