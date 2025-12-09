def rotate_arr(nums, k):
    nums[:len(nums)-k] = nums[:len(nums)-k][::-1]
    nums[len(nums)-k:] = nums[len(nums)-k:][::-1]
    return nums[::-1]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_arr(nums, k))