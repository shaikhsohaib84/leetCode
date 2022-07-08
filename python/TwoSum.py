'''
    **** TWO SUM ****
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
'''

def two_sum(lst, n):
    dic = {}
    temp = set()
    arr = []
    for idx, val in enumerate(lst):
        dic[val] = idx
    
    for idx, val in enumerate(lst):
        num = n-val
        if dic.get(num) and dic.get(num) != idx:
            if not(lst[idx] in temp and lst[dic.get(num)] in temp):
                temp.add(lst[idx])
                temp.add(lst[dic.get(num)])
                arr.extend([idx, dic.get(num)])
    print(temp)

lst = [1,2,3,4,5]
n = 6
two_sum(lst, n)

