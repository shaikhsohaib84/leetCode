lst = [1,2,3]
l = [-1,-1,-1,-1,-1,0]

def pivotIndex(nums):
    left_sum = 0
    total = sum(nums)

    for idx, val in enumerate(nums):
        right_sum = total - val - left_sum
        if left_sum == right_sum: return idx
        left_sum += val
        
res = pivotIndex(l)
print(res)