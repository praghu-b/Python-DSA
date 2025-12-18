# find the maximum elements of sliding window k in a contiguous sequence

def max_windows(nums, k):
    res = []
    
    for i in range(len(nums) + 1 - k):
        if len(nums) < k or i > len(nums) - k:
            return res
        
        max_ele = float('-inf')
        
        for j in range(i, i + k):
            if nums[j] > max_ele:
                max_ele = nums[j]
                
        if max_ele != float('-inf'): res.append(max_ele)
                
    return res
    
    
nums = [1,2,3]
k = 0
print(max_windows(nums, k))