'''
    If you start walking from north then whatever block you travers it should be same while returning to the
    back of your direction's.
    ex: head north -> 2 times then, you have to come back 2 time from south to north actuall starting position.
'''
# arr = ['n', 's', 'e', 'w', 'n', 'w', 'e', 'n', 'w', 's']
a1 = ['s', 'e', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']
a2 = ['e', 'w', 'e', 'w', 'n', 'e', 'n', 's', 'e', 'w']
a3 = ['s', 'e', 'w', 'n', 'e', 's', 'e', 'w', 'n', 's']

b = ['s', 'n', 'w', 'n', 'n', 's', 'e', 'w', 'n', 's']

def is_valid_walk(walk):
    #determine if walk is valid
    
    if len(walk) != 10:
        return False
    else:
        if (walk.count('n') == walk.count('s')) & (walk.count('e') == walk.count('w')):
            return True
        return False

print(is_valid_walk(b))