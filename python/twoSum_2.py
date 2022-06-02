arr =  [2,5,5,11]  # [3, 2, 3], [3,2,4], [2,5,5,11]
target = 10 # 6,6,10

def chk_diff(arr, diff, idx):
    if diff in arr:
        return arr.index(diff) + idx + 1
    return None

def two_sum(nums, target):
    lst = []
    if not nums: return []
    for idx in range(len(arr)):
        diff = target - arr[idx]
        res = chk_diff(nums[idx+1:], diff, idx)
        if res:
            return [idx, res]
        continue
    return lst
res = two_sum(arr, target)
print(res)

# total = nums[0]
#     for idx in range(1, len(nums)): # for idx, val in enumerate(nums, start=1):
#         if total + nums[idx] == target:
#             return [nums.index(total), idx]
#         total = nums[idx]