# lst = [3,4,1,5, 11, 7,6]
# num = 7

# # 7-3 = 4

# def pair(lst, target):
#     res_lst = []
#     res_dict = {
        
#     }

#     for idx, val in enumerate(lst):
#         n = target - val
#         if n not in res_dict:
#             res_dict[n] = val
#         else:
#             pass
        
#         # if n in lst:
#         #     res_lst.append([val, n])
#     print(res_dict)
#     return res_lst

# print(pair(lst, num))

# [val for val in lst if val % 2 == 0]



# try:
#     raise('err in api call ')

# except Exception as e;
#     ret
# finally:
#     pass

def printPairs(arr, arr_size, sum):
      
    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap = {}
      
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if (temp in hashmap):
            print (f'Pair with given sum {sum} is ({temp},{arr[i]}) at indices ({hashmap[temp]},{i})')
        hashmap[arr[i]] = i
  
# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16

A = [3,4,1,5,7,6]
n = 7

printPairs(A, len(A), n)
