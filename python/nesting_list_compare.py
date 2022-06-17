def lst_chk(lst1, lst2, flag):
    if not lst1 or not lst2 or len(lst1) != len(lst2): return False
    
    for val, idx in zip(lst1, lst2):
        if isinstance(val, list) and isinstance(idx, list) and len(val) == len(idx):
            flag = lst_chk(val, idx, True)
        elif isinstance(val, int) and isinstance(idx, int) or len(str(idx)) == len(str(val)):
            flag = True
            continue
        else: 
            flag = False 
            break
    return flag
        
        

# lst1 = [ [ [ ], [ ] ] ]
# lst2 = [ [ 1, 1 ] ]
# lst1 = [ 1, 1, 1 ] # True
# lst2 = [ 2, 2, 2 ] # True
# lst1, lst2 = [ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] #True

# lst1, lst2 = [ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] # False
# lst1, lst2 = [ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] # False
# lst1, lst2 = [ 1, [ 1, 1 ] ], [ 2, [2] ] # False

# lst1, lst2 = [ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] # True
# lst1, lst2 = [ [ [ ], [ ] ] ], [ [ 1, 1 ] ] # False

# lst1, lst2 = [1,[1,1]], [2,[2]] # False

# lst1, lst2 = [1,'[',']'], ['[',']',1] # True
lst1, lst2 = [19, -13, -4, 17], [9, -9, 7, 16, 13, -4, 18, 4, -6, [[[2, 10], -9, [19, -8], 9], []], 12, 10, 1, [[-5, -3, [15, -5, -20, [[-19, 10], [5, -3], 14, -8]], 4], 4, [-5, -15, -13, 11], [-8, [13, -18], 4, 3]], -5, 4, 10, -13, 12, -20, 16, 7, [7, [[18, -7], -15], -7, -7], [-14, -9, 6, -5], -12, -20] 

res = lst_chk(lst1, lst2, False)
print(res)