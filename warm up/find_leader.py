def find_leader(nums):
    leaders = []
    max_lead = float('-inf')
    
    for num in nums[::-1]:
        if num > max_lead:
            leaders.append(num)
            max_lead = num

    return leaders[::-1]
        
    

nums = [16, 17, 4, 3, 5, 2]
print(find_leader(nums))