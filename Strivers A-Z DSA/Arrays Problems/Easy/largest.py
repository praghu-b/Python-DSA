def largest(nums):
    lg = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > lg:
            lg = nums[i]

    return lg

nums = [2,5,1,3,0]
print(largest(nums))