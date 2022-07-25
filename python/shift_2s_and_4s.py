lst = [1,3,2,4,6]
res = []

for idx, val in enumerate(lst):
    if val==2:
        lst.insert(0, val)
        lst.pop(idx)
    elif val == 4:
        lst.insert(len(lst), val)
        lst.pop(id)
    else:
        # res.append(val)
        pass

print('res', lst)