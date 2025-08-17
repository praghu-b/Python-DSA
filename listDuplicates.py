def find_duplicates(nums):
    duplicates = []

    for i in nums[:-1]:
        for j in nums[i+1:]:
            if i == j and i not in duplicates:
                duplicates.append(i)
    
    return duplicates

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 6, 7, 8]
result = find_duplicates(nums)
print(result)