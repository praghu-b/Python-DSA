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
    

nums = [-100000,50000,50000,0]
print(three_sum(nums))