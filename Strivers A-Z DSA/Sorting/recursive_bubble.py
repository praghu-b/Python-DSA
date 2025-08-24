def bubble(nums, n):
    if n <= 1:
        return nums
    
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        
    return bubble(nums, n-1)


nums = [13,46,24,52,20,9]
print(bubble(nums, len(nums)))