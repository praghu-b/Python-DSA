def two_sum_brute(nums, k):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == k:
                return [i, j]
            
    return [-1, -1]

# Time - O(n^2) & Space - O(1)

def two_sum_hash(nums, k):
    nums_set = {value: index for index, value in enumerate(nums)}

    for i in range(len(nums)):
        if k-nums[i] in nums_set:
            return [i, nums_set[k-nums[i]]]
        
    return [-1, -1]

# Time - O(2n) & Space - O(n)

def two_sum_2pointer(nums, k):
    nums_sort = [(num, i) for i,num in enumerate(nums)]
    nums_sort.sort(key= lambda x: x[0])

    i, j = 0, len(nums)-1

    while i < j:
        if nums_sort[i][0] + nums_sort[j][0] == k:
            return [nums_sort[i][1], nums_sort[j][1]]
        elif nums_sort[i][0] + nums_sort[j][0] < k:
            i+=1
        else:
            j-=1

    return [-1, -1]

# Time - O(n) & Space - O(1)    

nums = [2, 6, 5, 8, 11]                     # [2, 5, 6, 8, 11]
print(two_sum_2pointer(nums, 19))