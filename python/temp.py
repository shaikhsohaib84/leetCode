def find_pivot(lst, key, left, right):
    pivot = (left + right) // 2
    first_lst_value = lst[0]
    if lst[pivot] == key: return pivot
    elif first_lst_value > key:
        left = pivot + 1
        binary_search(lst, key, left, right)
    elif first_lst_value < key:
        right = pivot - 1
        binary_search(lst, key, left, right)
    else: return -1
    
def binary_search(lst, key, left, right):
    find_pivot(lst, key, left, right)
    
def driver(lst):
    binary_search(lst, 4, 0, len(lst) - 1)

arr = [3,4,5,1,2]
res = driver(arr)
print(res)