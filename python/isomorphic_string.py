def isomorphic_string(string_1, string_2):
    # string_dict = {}
    # if not string_1 or not string_2: return False
    # if len(string_1) != len(string_2): return False
    
    # for char_1, char_2 in zip(string_1, string_2):
    #     if char_1 not in string_dict and char_2 not in string_dict:
    #         string_dict[char_1] = char_2
    #         continue
    #     if string_dict.get(char_1) == char_2:
    #         continue
    #     return False
    # return True
    if len(string_1) != len(string_2):
        return False
    else:
        map1, map2 = {}, {}
        for i in range(len(string_1)):
            ch1, ch2 = string_1[i], string_2[i]
            if ch1 not in map1:
                map1[ch1] = ch2
            if ch2 not in map2:
                map2[ch2] = ch1
            if map1[ch1] != ch2 or map2[ch2] != ch1:
                return False
    return True

string_1 = "bbbaaaba" # 'foo' 'paper' 'badc'
string_2 = "aaabbbba" # 'bar' 'title' 'baba'

res = isomorphic_string(string_1, string_2)
print(res)