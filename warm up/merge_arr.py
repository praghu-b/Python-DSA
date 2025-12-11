def merge_sort_arr(arr1, arr2, m, n):
    i = m - 1
    j = n - 1
    k = len(arr1) - 1

    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1

        k -= 1
        
    return arr1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
print(merge_sort_arr(nums1, nums2, 3, 3))  
