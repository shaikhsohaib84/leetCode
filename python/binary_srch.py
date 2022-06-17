def arr_pivot_index(lst):
    temp = 0
    for idx, val  in enumerate(lst):
        if temp == 0:
            temp = val
            continue
        if temp - val == -1:
            temp = val
        else:
            return idx

def binary_search(lst, key):
    if not lst: return -1
    lst_len = len(lst)
    pivot = lst_len // 2
    if lst[pivot] == key:
        return pivot
    elif lst[pivot] > key:
        return binary_search(lst[:pivot], key)
    elif lst[pivot] < key:
        return binary_search(lst[pivot:], key)
    else: return -1

def find_key(left_lst, right_lst, key):
    left_search = binary_search(left_lst, key)
    right_search = binary_search(right_lst, key)
    if left_search != -1:
        return left_search
    return right_search

def sorted_roated_binary_search(lst, key):
    index = arr_pivot_index(lst)
    left_lst = lst[:index]
    right_lst = lst[index:]
    return find_key(left_lst, right_lst, key)
        

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3
print(sorted_roated_binary_search(arr, key))