a = [123, -123, 120, 0, -10, 901000, 1534236469]

def reverseInteger(num):
    if int(str(abs(num))[::-1]) > pow(2, 31): return 0
    elif num > 0:
        return int(str(num)[::-1])
    elif num < 0:
        return int('-' + str(num).split('-')[1][::-1])
    else: return 0


reverseInteger(901000)
