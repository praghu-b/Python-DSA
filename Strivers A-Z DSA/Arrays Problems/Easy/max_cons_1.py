def max_cons(nums):
    max = 0
    n = 0

    for i in range(len(nums)):
        if nums[i] == 1:            
            n += 1
            if n > max:
                max = n
        else:
            n = 0

    return max
        

nums = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
print(max_cons(nums))