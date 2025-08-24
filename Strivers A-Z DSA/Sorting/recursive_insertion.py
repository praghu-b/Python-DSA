def recursive_insertion(nums, n, i):
    if n == i:
        return nums
    
    j = i

    while nums[j] < nums[j-1] and j > 0:
        nums[j], nums[j-1] = nums[j-1], nums[j]
        j-=1

    return recursive_insertion(nums, n, i+1)


nums = [13,46,24,52,20,9]
print(recursive_insertion(nums, len(nums), 1))