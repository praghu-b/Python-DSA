def bubble(nums):
    itr = len(nums) - 1
    for i in range(itr):
        for j in range(itr-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

    return nums


nums = [13,46,24,52,20,9]
print(bubble(nums))