def intersection(arr1, arr2):
    i = j = 0
    n1, n2 = len(arr1), len(arr2)
    inter = []

    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            if len(inter) == 0 or inter[-1] < arr1[i]:
                inter.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1

    return inter

arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5,6]
print(intersection(arr1, arr2))