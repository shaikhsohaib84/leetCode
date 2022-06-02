class Solution:
    def containsDuplicate(self, nums):
        set_nums = set(nums)
        return False if len(set_nums) == len(nums) else True

l = [0,4,5,0,3,6]

obj = Solution()
print(obj.containsDuplicate(l))
