def track_count(nums, int_arr):
    set_arr = dict.fromkeys(nums, 0)

    for i in int_arr:
        if i in set_arr:
            set_arr[i] += 1

    return set_arr
    

nums = [ 1,3,4,2,10 ]
int_arr = [ 1,2,1,3,2 ]
print(track_count(nums, int_arr))