def max_sum_sarr(nums):
    max = nums[0]

    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        sum=nums[i]
        if sum > max:
            max = sum
        for j in range(i+1, len(nums)):
            sum += nums[j]
            if sum > max:
                max = sum
    
    return max

# Time - O(n^2) & Space - O(1)

def kadane_algo(nums):
    max_sum = nums[0]
    cur_sum = 0
    start_sub = 0
    end_sub = 0

    for i in range(len(nums)):
        cur_sum += nums[i]
        if max_sum < cur_sum:
            max_sum = cur_sum
            end_sub = i
        if cur_sum < 0:
            cur_sum = 0
            start_sub = i+1

    if max_sum < 0:
        return [max_sum], max_sum

    return nums[start_sub: end_sub+1], max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algo(nums))