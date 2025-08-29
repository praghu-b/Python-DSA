def rotate_left1(nums):
    one = nums[0]

    for i in range(1, len(nums)):
        nums[i-1] = nums[i]
    
    nums[-1] = one

    return nums

nums = [1,2,3,4,5]
print(rotate_left1(nums))