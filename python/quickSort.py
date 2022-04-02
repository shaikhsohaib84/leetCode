def partition(start, end, arr):
    pi_idx = start
    pi = arr[pi_idx]

    while start < end:
        while start < len(arr) and arr[start] <= pi:
            start += 1
        
        while arr[end] > pi:
            end -= 1
         
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    
    arr[end], arr[pi_idx] = arr[pi_idx], arr[end]

    return end

def quick_sort(start, end, arr):
    if start < end:
        p = partition(start, end, arr)
        quick_sort(start, p-1, arr)
        quick_sort(p+1, end, arr)



if __name__ == '__main__':
    arr = [10, 80, 30, 90, 40,50, 70]
    quick_sort(0, len(arr)-1, arr)
    print(arr)
    