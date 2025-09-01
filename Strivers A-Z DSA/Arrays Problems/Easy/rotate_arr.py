def rotate_left(nums, k):
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
    nums.reverse()


def rotate_right(nums, k):
    nums[-k:] = nums[-k:][::-1]
    nums[:-k] = nums[:-k][::-1]
    nums.reverse()


def rotate(n,nums,k,dir):
    if k > n:
        k = k % n
    if dir=='right':
        rotate_right(nums, k)
    else:
        rotate_left(nums, k)


nums = [1,2,3,4,5,6,7]
rotate(len(nums),nums,10,'right')
print(nums)