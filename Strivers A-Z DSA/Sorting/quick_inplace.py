def quick(nums, low, high):
    
    if low < high:
        pi = partition(nums, low, high)
        quick(nums, low, pi-1)
        quick(nums, pi+1, high)


def partition(nums, low, high):

    pivot = nums[high]
    i = low-1

    for j in range(low, high):
        if nums[j] <= pivot:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i+1], nums[high] = nums[high], nums[i+1]

    return i+1


nums = [4, 6, 7, 5, 2, 9, 1, 3]
quick(nums, 0, len(nums)-1)
print(nums)