a = [123, -123, 120, 0, -10, 901000]

def reverseInteger(num):
    if num > 0:
        res = ''.join(reversed(str(num)))
        if "0" in res:
            res = res.replace("0", '')
        print(res)
    elif num < 0:
        pos = str(num).split('-')[1]
        res = ''.join(reversed(pos))
        print(f"-{res}")
    else:
        print(0)


reverseInteger(901000)
