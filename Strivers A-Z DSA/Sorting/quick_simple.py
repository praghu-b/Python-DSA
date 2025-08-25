def quick(nums):
    if len(nums) <= 1:
        return nums
    
    i = -1
    pivot = nums[i]

    for j in range(len(nums)-1):
        if nums[j] < pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[-1] = nums[-1], nums[i+1]

    return quick(nums[:i+1]) + [nums[i+1]] + quick(nums[i+2:])


nums = [4,6,7,5,2,9,1,3]
print(quick(nums))