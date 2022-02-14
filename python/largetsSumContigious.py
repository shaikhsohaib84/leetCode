# l = [-2,1,-3,4,-1,2,1,-5,4]
l = [-2, -1]

class Solution:
    def larget_sum(self, list):
        lst = sorted(list)
        max1 = lst[0]
        max2 = 0

        for item in list:
            max2 = max2 + item

            if max2 < 0: max2=0

            elif max1 < max2:
                max1 = max2
            
        return max1

obj = Solution()
print(obj.larget_sum(l))