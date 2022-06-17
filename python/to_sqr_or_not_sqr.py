import math

def is_square(elem):
    root = math.sqrt(elem)
    is_sq_root = (int(root + 0.5) ** 2)
    return int(root) if is_sq_root == elem else elem ** 2

def square_or_square_root(arr):
    res = list(map(is_square, arr))
    return res