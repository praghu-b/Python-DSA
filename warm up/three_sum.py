def three_sum_bf(nums):
    res = []
    nums.sort()
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    sub_arr = [nums[i], nums[j], nums[k]]
                    if sub_arr not in res:
                        res.append(sub_arr)
                    
    return res

def three_sum_opt(nums):
    nums.sort()
    res = []
    n = len(nums)
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        if nums[i] > 0:
            break
        
        j = i + 1
        k = n - 1
        
        while j < k:
            if nums[j] + nums[k] + nums[i] == 0:
                res.append([nums[i], nums[j], nums[k]])
                    
                j += 1
                k -= 1
                
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
                
            elif nums[j] + nums[k] + nums[i] < 0:
                j += 1
            else:
                k -= 1
        
    return res


nums = [-100000,50000,50000,0]
print(three_sum_opt(nums))