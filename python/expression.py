'''
    remove consecutive char from the given string
'''
input_string = "abbbcdd"

def chk_string(input_string):
    new_str = ''
    for char in input_string:
        if char not in new_str:
            new_str += char
    return new_str


print(chk_string(input_string))