# lst = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
lst = [2,3,1,1,2,4,2,0,1,1]

class Solution:
    def __init__(self):
        self.cnt = 0
        self.arr = []
        self.pos_dict = {}
        
    def minJumps(self, arr):
        self.arr = arr
        for idx, val in enumerate(arr):
            self.pos_dict[idx] = val
        return self.jump(0)
    
    def jump(self, idx=0):
        val = self.pos_dict[idx]
        if val == 0: return -1
        if val > idx:
            self.cnt += 1
            self.jump(val)
        return self.cnt

res = Solution()
print(res.minJumps(lst))