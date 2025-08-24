def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

nums = [12, 11, 13, 5, 6, 7]
print(merge_sort(nums))