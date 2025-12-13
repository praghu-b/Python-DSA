# Generate product of array except self

def prod_arr(nums):
    res = []
    
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        res.append(prod)        
        
    return res


nums = [1000,100,10,2]
print(prod_arr(nums))