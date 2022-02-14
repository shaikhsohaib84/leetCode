class Solution:
    def containsDuplicate(self, nums):
        nums_dict = dict()
        flag = True
        
        for data in nums:
            if data not in nums_dict:
                nums_dict[data] = data
                flag = False
            else: 
                flag = True
                break
         
        return flag

l = [0,4,5,0,3,6]

obj = Solution()
print(obj.containsDuplicate(l))
