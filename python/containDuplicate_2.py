class containDuplicate:
    def duplicate(self, nums, num):
        is_true = False
        num_dict = {} # key: array element, value: array index
        for index, elem in enumerate(nums):
            if elem not in num_dict:
                num_dict[elem] = index
                continue
            is_true = abs(num_dict[elem] - index) <= num
            if is_true: return is_true
            num_dict[elem] = index
        return is_true

        

# nums, num = [1,2,3,1], 3
# nums, num = [1,0,1,1], 1
nums, num = [1,2,3,1,2,3], 2
obj = containDuplicate()
result = obj.duplicate(nums, num)
print(result)