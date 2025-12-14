# Find the container with maximum water, where the difference between two indices is distance.

def max_water(nums):
    max_area = 0
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            distance = j - i
            area = min(nums[i], nums[j]) * distance
            
            if area > max_area:
                max_area = area
                
    return max_area
            

nums = [1,8,6,2,5,4,8,3,7]
print(max_water(nums))