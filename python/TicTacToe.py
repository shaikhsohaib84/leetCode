# lst = [[2, 1, 1],
#  [2, 1, 1],
#  [1, 2, 2]]

# lst = [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]

# lst = [[1, 1, 1],
#          [0, 2, 2],
#          [0, 0, 0]]

# lst = [[2, 1, 2],
#          [2, 1, 1],
#          [1, 1, 2]]

lst = [[2, 1, 2],
         [2, 1, 1],
         [1, 2, 1]]

class Game:
    def __init__(self, arr=[]):
        self.arr = arr
        if self.isXWon():
            self.res = 1
        elif self.isOOwn():
            self.res = 2
        elif self.checkIsEmpty():
            self.res = -1
        else:
            self.res = 0

        
    def checkIsEmpty(self):
        for sub_arr in self.arr:
            if 0 in sub_arr:
                return True
        return False
    
    def vertical(self, flag):
        for sub_arr in self.arr:
            res = all(val == flag for val in sub_arr)
            if res: return True
        return False
    
    def horizontal(self, flag):
        col = 0

        while col < len(self.arr):
            temp_arr = []
            for idx, lst in enumerate(self.arr):
                temp_arr.append(self.arr[idx][col])
            if all(val == flag for val in temp_arr): return True
            col +=1
        return False

    def right_digonal(self, flag):
        row, col = 0,0
        temp_arr = []
        while row < len(self.arr) and col < len(self.arr):
            temp_arr.append(self.arr[row][col])
            row += 1
            col += 1
        return all(val == flag for val in temp_arr)
    
    def left_digonal(self, flag):
        n = len(self.arr)
        row = 0
        col = n - 1
        temp_arr = []
        while row < n:
            temp_arr.append(self.arr[row][col])
            row += 1
            col -= 1
        return all(flag == val for val in temp_arr)
    
    def isXWon(self):
        if self.vertical(1) or self.horizontal(1) or self.right_digonal(1) or self.left_digonal(1):
            return True
        return False

    def isOOwn(self):
        if self.vertical(2) or self.horizontal(2) or self.right_digonal(2) or self.left_digonal(2):
            return True
        return False
        
    
        
res = Game(lst)
print('res', res.res)