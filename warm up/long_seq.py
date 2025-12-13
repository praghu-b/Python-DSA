# Longest Consecutive Sequence

def longest_consecutive(nums):
    sorted = set(nums)
    max_count = 0
    
    for num in nums:
        if num-1 not in sorted:
            count = 1
            while num+count in sorted:
                count += 1
            max_count = max(max_count, count)
    
    return max_count


nums = [10, 5, 6, 7, 3, 4]
print(longest_consecutive(nums))