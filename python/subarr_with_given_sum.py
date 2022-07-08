lst1 = [10, 12, 2, 4, 13, 19, 5]
num1 = 18

lst2 = [1,2,3,7,5]
num2 = 12

lst3 = [1,2,3,4,5,6,7,8,9,10]
num3 = 15

lst4 = [1,2,3,7,5]
num4 = 122

lst5 = [
    135, 101, 170, 125, 79, 159, 163, 65, 106, 146, 82, 28, 162, 92, 
    196, 143, 28, 37, 192, 5, 103, 154, 93, 183, 22, 117, 119, 96, 
    48, 127, 172, 139, 70, 113, 68, 100, 36, 95, 104, 12, 123, 134]
num5 = 468

def find_pos(lst, num):
    sum_val = 0
    n = len(lst)
    for val_1 in range(n):
        sum_val = lst[val_1]
        for val_2 in range(val_1+1, n):
            if sum_val == num: 
                return val_1+1, val_2
            if sum_val > num: break
            sum_val += lst[val_2]
    return -1

res5 = find_pos(lst2, num2)
print(res5) 