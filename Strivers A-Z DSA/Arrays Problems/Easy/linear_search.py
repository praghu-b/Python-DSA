def linear_search(nums,target):
    if len(nums) < 1:
        return -1
    
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return -1


nums = [1,2,3,4,5,6,7]
print(linear_search(nums, 6))