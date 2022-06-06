def missing_num_in_arr(arr, start, end):
    total_sum, arr_sum  = 0, 0
    arr_sum=sum(arr)
    for val in range(start, end+1):
        total_sum += val
    return total_sum-arr_sum

arr, start, end = [1,2,3,5,6], 1, 6 # missing num is 4
res = missing_num_in_arr(arr, start, end)
print(f'Missing number is {res}')