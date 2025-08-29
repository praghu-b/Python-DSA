def second_lg(nums):
    if len(nums) < 2:
        return -1

    largest = float('-inf')
    second_lg = float('-inf')

    for i in range(len(nums)):
        if nums[i] > largest:
            second_lg = largest
            largest = nums[i]
        elif largest > nums[i] > second_lg:
            second_lg = nums[i] 

    return second_lg if second_lg != float('-inf') else -1


def second_sm(nums):
    if len(nums) < 2:
        return -1
    
    smallest = float('inf')
    second_sm = float('inf')

    for i in range(len(nums)):
        if nums[i] < smallest:
            second_sm = smallest
            smallest = nums[i]
        elif smallest < nums[i] < second_sm:
            second_sm = nums[i]

    return second_sm if second_sm != float('inf') else -1


nums = [1,2,4,7,7,5]
print('Second Largest: ', second_lg(nums))
print('Second Smallest: ', second_sm(nums))