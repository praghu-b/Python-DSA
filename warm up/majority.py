def find_mjr_element(nums):
    count = {}
    max_count = 0
    mjr = 0

    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    for item in count:
        if count[item] > max_count:
            max_count = count[item]
            mjr = item

    if count[mjr] > len(nums)//2: return mjr

    return 0
    

nums = [2,1,1,1,1,3,3]
print(find_mjr_element(nums))