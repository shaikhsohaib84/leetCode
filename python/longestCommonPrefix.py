arr = ["flower", "flight", "flow"]

def lcp(arr):
    size = len(arr)
    if size == 0: return ""
    if size == 1: return []
    
    arr.sort()
    
    start = 0
    end = min(len(arr[0]), len(arr[size-1]))
    
    while start < end and arr[0][start] == arr[size-1][start]:
        start += 1

    string = arr[0][:start]
    return string    

res = lcp(arr)
print(res)
