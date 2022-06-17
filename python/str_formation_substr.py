import collections
def is_repeated(string):
    results = collections.Counter(string)
    lst = list(dict(results).values()) or []
    min_val = min(lst)
    total_val = sum(lst)
    lst.remove(min_val)
    for val in lst:
        if val %  min_val == False: return 1
    return 0

# string = "adch"
# string = "ababac"
# string = "knouknout"
# string = "qqsqqsqqs"
# string = "jyqjyqqjyq"
# string = "abadabad"
string = "gtgtgtfgt"
# string = "ababab"
# string = "ybybyb"
print(is_repeated(string))