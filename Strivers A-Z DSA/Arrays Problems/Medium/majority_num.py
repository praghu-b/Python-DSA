def mjr_num(nums):
    k = len(nums)//2
    count_dict = dict.fromkeys(nums, 0)
    mjr = 0

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
    
    for num in count_dict:
        if count_dict[num] > k:
            k = count_dict[num]
            mjr = num

    return mjr

# Time - O(n) & Space - O(n)

# Moore's Voting Algorithm

def mjr_num_mva(nums):
    k = len(nums)//2
    count = 0
    element = 0

    for i in range(len(nums)):
        if count == 0:
            element = nums[i]
            count+=1
        elif nums[i] == element:
            count+=1
        else:
            count-=1

    count1 = 0
    for i in range(len(nums)):
        if nums[i] == element:
            count1+=1

    if count1 > k:
        return element
    
    return -1

# Time - O(n) & Space - O(1)


nums = [4,4,2,4,3,4,4,3,2,4]
print(mjr_num_mva(nums))