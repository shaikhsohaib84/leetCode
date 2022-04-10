from math import gcd

def lcm(*args):
    lcm = 1
    for i in args:
        try:
            lcm = lcm*i//gcd(lcm, i)
        except ZeroDivisionError:
            lcm = 0
    return lcm

print(lcm(2,5))
# print(lcm(0,1))
# print(lcm(5, 6, 7, 9, 6, 9, 18, 4, 5, 15, 15, 10, 17, 7))