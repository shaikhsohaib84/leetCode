# arr = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9],
#     ]
# 1 2 3 6 9 8 7 4 5

# arr = [
#         [1,2,3,4],
#         [5,6,7,8],
#         [9,10,11,12],
#     ] 
# 1 2 3 4 8 12 11 10 9 5 6 7

arr = [
    [1,2,3,1],
    [4,5,6,4],
    [7,8,9,7],
    [7,8,9,7]
]

class snail_sort:
    right, bottom, left, top = 1, 1, 1, 1
    def __init__(self, arr):
        self.arr = arr
        self.result_arr = []
        self.flag = True
        res = self.driver()
        return res
    
    def driver(self):
        global right, bottom, left, top
        while self.flag:
            right = self.right()
            if not right: break
            bottom = self.bottom()
            if not bottom: break
            left = self.left()
            if not left: break
            top = self.top()
            if not top: break
        return self.result_arr
    
    def right(self):
        if not self.arr: return False

        for right_val in self.arr[0]:
            self.result_arr.append(right_val)
        self.arr.remove(self.arr[0])
        return 1

    def bottom(self):
        try:
            if not self.arr: return False

            for bottom_val in self.arr:
                self.result_arr.append(bottom_val[-1])
                bottom_val.remove(bottom_val[-1])
            return 1
        except Exception as e:
            print(e)
            return None

    def left(self):
        try:
            if not self.arr: return False

            for left_val in self.arr[-1][::-1]:
                self.result_arr.append(left_val)
            self.arr.remove(self.arr[-1])
            return 1
        except Exception as e:
            print(e)
            return None

    def top(self):
        try:
            if not self.arr: return False

            for right_val in self.arr[-1]:
                self.result_arr.append(right_val)
                self.arr[-1].remove(right_val)
            return 1
        except Exception as e:
            print(e)
            return None
    
res = snail_sort(arr)
print(res)