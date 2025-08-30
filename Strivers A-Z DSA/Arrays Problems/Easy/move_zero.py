def move_zero(nums):
    i = -1

    for j in range(len(nums)):
        if nums[j] != 0:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]

    return nums


nums = [0,1,0,2,3,2,0,0,4,5,1]
print(move_zero(nums))