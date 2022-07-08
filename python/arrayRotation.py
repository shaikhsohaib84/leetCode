# Rotation of the above array by 2 will make an array

lst = [1, 2, 3, 4, 5, 6, 7]
rotate_by = 2

print(lst[rotate_by:] + lst[0:rotate_by])