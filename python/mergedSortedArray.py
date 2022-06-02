ar1 = [1,2,3,0,0,0] # [1,2,3,0,0,0], [1]
ar2 = [2,5,6] # [2,5,6], []

def sort_arr(nums1, nums2):
    nums1 = list(filter(None, nums1))
    for elem in nums2:
        if elem in nums1:
            nums1.insert(nums1.index(elem), elem)
        else:
            nums1.append(elem)
    return nums1
res = sort_arr(ar1, ar2)
print(res)