def find_common(nums1, nums2):
    common = set()
    seen = set()

    for num in nums1:
        seen.add(num)

    for num in nums2:
        if num in seen and num not in common:
            common.append(num)

    return common

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(find_common(nums1, nums2))