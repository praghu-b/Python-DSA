def sum_list(arr):
    sum = 0
    
    for i in arr:
        sum+=i

    return sum


arr = [1,2,3,4,5]
result = sum_list(arr)
print(result)