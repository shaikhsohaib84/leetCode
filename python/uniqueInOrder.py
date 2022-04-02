def unique_in_order(string):
    lst = []
    temp = string[0]
    for char in string:
        if char == temp:
           
            lst.append(temp)
            temp = char
    lst.append(temp)
    return lst
