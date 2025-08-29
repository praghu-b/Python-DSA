def remove_duplicates(nums):
    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]

    for j in range(i+1, len(nums)):
        nums[j] = '_'

    return nums

nums = [1,2,3,3,4,5,5]
print(remove_duplicates(nums))