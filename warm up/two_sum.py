# Two Sum

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        seen[nums[i]] = i   

    for num in nums:
        if target-num in seen:
            return [seen[num], seen[target-num]]

    return 0
        



nums = [4,4]
target = 8
print(two_sum(nums, target))