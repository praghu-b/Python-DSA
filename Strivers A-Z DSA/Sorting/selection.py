def sort(n):
    nums = n
    
    for i in range(len(nums)-1):
        min = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        
        if min != i:
            temp = nums[i]
            nums[i] = nums[min]
            nums[min] = temp

    return nums



nums = [13,46,24,52,20,9]
print(sort(nums))