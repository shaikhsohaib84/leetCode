def merge_sort(lst):
    lst_len = len(lst)
    if lst_len > 1:    
        mid = lst_len // 2
        l = lst[:mid]
        r = lst[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i<len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k] = l[i]
                i += 1
            else:
                lst[k] = r[j]
                j += 1
            k += 1
        
        while i < len(l):
            lst[k] = l[i]
            i += 1
            k += 1
        
        while j < len(r):
            lst[k] = r[j]
            j += 1
            k += 1


if __name__ == '__main__':
    ms = [8, 4, 2, 1]
    merge_sort(ms)
    print(ms)