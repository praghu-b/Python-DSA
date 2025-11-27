# Check if an array is sorted (non-decreasing).

def is_sorted(arr):
    if len(arr) == 1:
        return True
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

arr1 = [3, 4, 2, 5, 1, 9, 7, 6, 8] 
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(is_sorted(arr1))