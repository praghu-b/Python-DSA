# find how many subarray's sum is equal to k

def count_subarr_sum(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum == k:
                count += 1

    return count


nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(count_subarr_sum(nums, k))