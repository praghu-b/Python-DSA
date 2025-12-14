# Find the container with maximum water, where the difference between two indices is distance.

def max_water_bf(nums):
    max_area = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            distance = j - i
            area = min(nums[i], nums[j]) * distance
            
            if area > max_area:
                max_area = area
                
    return max_area
            
def max_water_opt(nums):
    max_area = 0
    i = 0
    j = len(nums) - 1
    
    while i < j:
        distance = j - i
        area = min(nums[i], nums[j]) * distance
        
        if area > max_area:
            max_area = area
            
        if nums[i] > nums[j]:
            j -= 1
        else:
            i += 1
            
    return max_area


nums = [2,3,10,5,7,8,9]
print(max_water_opt(nums))