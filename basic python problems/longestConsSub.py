# Finding the longest consecutive subsequence in list

def lgt_cons_subseq(nums):
    nums_set = set(nums)
    max_count = 0
    
    for num in nums_set:

        if num-1 not in nums_set:
            current = num
            count = 1

            while current+1 in nums_set:
                count+=1
                current+=1

            max_count = max(max_count, count)

    return max_count


nums = [100, 4, 200, 1, 3, 2]
result = lgt_cons_subseq(nums)
print(result)