def is_sorted(nums):
    if len(nums) < 1:
        return False

    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            return False
        
    return True

# nums = [1,2,3,4,5]
nums = [1,3,7,2,9]
print(is_sorted(nums))