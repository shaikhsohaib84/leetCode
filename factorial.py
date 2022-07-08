cnt = 1
def fun(n):
    global cnt
    if n == 0: 
        return cnt
    cnt = cnt * n
    fun(n-1)

fun(5)
print(cnt)