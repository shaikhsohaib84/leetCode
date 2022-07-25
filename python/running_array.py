def check_running_sum(func):
    def decorator(*args, **kwargs):
        lst = list(args[0])
        lst_size = len(lst)
        
        if not lst_size: return 0
        if lst_size == 1: return lst
        
        return func(*args, **kwargs)
    return decorator

@check_running_sum
def running_sum(lst):
    res_lst = []
    total = 0
    for val in lst:
        total += val
        res_lst.append(total)
    return res_lst

nums = [3,1,2,10,1]
res = running_sum(nums)
print(res)