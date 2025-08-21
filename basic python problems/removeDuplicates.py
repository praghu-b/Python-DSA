def remove_duplicates(nums):
    seen = set()

    for num in nums:
        if num not in seen:
            seen.add(num)
    
    return seen

duplicated_list = [1, 2, 3, 4, 2, 3, 5, 1, 6, 3, 4, 7, 8, 5, 6, 9, 1, 2]
result = remove_duplicates(duplicated_list)
print(result)