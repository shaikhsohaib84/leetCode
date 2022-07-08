from collections import Counter

exp = {
    '{' : '}',
    '}': '{',
    '(' : ')',
    ')':'(',
    '[' : ']',
    ']' : '['
}

exp_str = '{([])}' #'([)]'
def checker(exp_str):
    n = len(exp_str)-1
    i = 0
    j = n
    while i<n:
        if i > j: break
        if exp.get(exp_str[i]) != exp_str[j]: return False
        i += 1
        j -= 1
    return True
        
    # exp_dict = dict(Counter(exp_str))
    
    # for k, v in exp_dict.items():
    #     closing_char = exp.get(k)
        
    #     if exp_dict.get(k) != exp_dict.get(closing_char):
    #         return False
    #     return True
        
print(checker(exp_str))