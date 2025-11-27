# Find max & min in array 

nums = [3, 4, 2, 5, 1, 9, 7, 6, 8] 
mn = float('inf') 
mx = float('-inf') 

for num in nums: 
    if num > mx: 
        mx = num 
    if num < mn: 
        mn = num 
        
print(mn, mx)