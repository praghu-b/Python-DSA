def find_duplicates(nums):
    duplicates = []
    
    for i in range(len(nums)):
        index = abs(nums[i])-1
        if nums[index] < 0:
            duplicates.append(abs(nums[i]))
        else:
            nums[index] = -nums[index]

    return duplicates

nums = [4,3,2,7,8,2,3,1]
print(find_duplicates(nums))