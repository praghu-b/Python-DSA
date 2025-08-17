def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    
    return duplicates

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 6, 7, 8]
result = find_duplicates(nums)
print(result)