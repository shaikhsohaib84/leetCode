class LongestSubstring:
    '''
        **** Longest Substring Without Repeating Characters ****

        Given a string s, find the length of the longest substring without repeating characters.
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        
        ['abcabcbb', 'pwwkew', 'bbbbb', ' ', 'c', 'au', 'aab', "abcabcbb", 'dfdv']
    '''
    
    def __init__(self, string, newstr=''):
        self.string = string
        self.newstr = newstr

    def lengthOfLongestSubstring(self):
        final_dict = {}
        if len(self.string) == 1: return 1
        for char in self.string:
            if char not in self.newstr:
                self.newstr += char
            else:
                final_dict.update({self.newstr: len(self.newstr)})
                self.newstr = ''
                if char not in self.newstr:
                    self.newstr += char
        dict_max_len = len(max(final_dict, key=final_dict.get)) if final_dict else 0
        new_str_len = len(self.newstr)
        max_str_len = max(dict_max_len, new_str_len)

        
        return (max_str_len)


obj1 = LongestSubstring('dfdv')

final_str1 = obj1.lengthOfLongestSubstring()

print(final_str1)
