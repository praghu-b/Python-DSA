def merge_lists(list1, list2):
    final_list = []
    i = j = 0

    # sort the list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        else:
            final_list.append(list2[j])
            j += 1

    final_list.extend(list1[i:])
    final_list.extend(list2[j:])
            
    return final_list


list1 = [1, 5, 9, 14, 20, 25, 33, 40, 47, 50]
list2 = [2, 6, 10, 15, 18, 22, 28, 35, 44, 49]
result = merge_lists(list1, list2)
print(result)