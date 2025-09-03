def sort_inplace(nums):
    count_1 = count_2 = count_0 = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            count_1+=1
        elif nums[i] == 2:
            count_2+=1
        else:
            count_0+=1

    for i in range(count_0):
        nums[i] = 0
    for i in range(count_0, count_0 + count_1):
        nums[i] = 1
    for i in range(count_0 + count_1, count_0 + count_1 + count_2):
        nums[i] = 2

    return nums

# Time - O(n) & Space - O(1)

def sort_inplace_opt(nums):
    low = mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            low+=1
            mid+=1
        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1

    return nums

# Time - O(n) & Space - O(1)

nums = [2, 0, 0, 1, 2, 2, 1, 0, 1, 2]
print(sort_inplace_opt(nums))