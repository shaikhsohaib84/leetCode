def searchRange(nums, target):
   pass

def binarySearch(nums, target, searchLeft):
    l = 0
    r = len(nums)

    while l<=r:
        mid = (l+r) // 2
        if mid == target:
            

# arr = []
# target = 0

# arr = [5,7,7,8,8,10]
# target = 8

# arr = [2,1,3,1]
# target = 1

# arr = [1,3]
# target = 1

arr = [1,4]
target = 4

# arr = [1]
# target = 1

# arr = [1]
# target = 0
print(searchRange(arr, target))