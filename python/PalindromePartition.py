'''
    Palindrome Partitioning
    
    Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
    A palindrome string is a string that reads the same backward as forward.

    Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]
    
    Example 2:
    Input: s = "a"
    Output: [["a"]]

    name = Nitin, mam
'''
from collections import Counter
name = ''

counter_dict = Counter(name)
updated_dict = {}
temp_counter = 0


for key, value in counter_dict.items():
    if value >= temp_counter:
        temp_counter = value
        updated_dict[k] = name.find(key)

def chk_palindrome(key, value):
    new_char = ''
    new_char += key
    for char in name[value+1:]:
        if char != key:
            new_char += char
        else:
            new_char += char
            if new_char == new_char[::-1]: return new_char
            
        
for key, value in counter_dict.items():
    print(chk_palindrome(key, value))
        
