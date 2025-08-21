def sum_pairs(nums, target):
    pairs = []
    seen = set()

    for num in nums:
        needed = target - num
        if needed in seen:
            pairs.append((needed, num))
        else:
            seen.add(num)

    return pairs

nums = [2, 7, 11, 15, 1, 8, 3, 6]
target = 9
result = sum_pairs(nums, target)
print(result)