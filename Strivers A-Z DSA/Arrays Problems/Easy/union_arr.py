def union(arr1, arr2):
    i = j = 0
    n1, n2 = len(arr1), len(arr2)
    union = []

    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1

    while i < len(arr1):
        if union[-1] < arr1[i] and union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1

    while j < len(arr2):
        if union[-1] < arr2[j] and union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1

    return union


arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
print(union(arr1, arr2))