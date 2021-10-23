class LongestSubstring:
    '''
        **** Longest Substring Without Repeating Characters ****

        Given a string s, find the length of the longest substring without repeating characters.
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
        
        [abcabcbb, pwwkew, bbbbb]
    '''
    
    def __init__(self, string, newstr=''):
        self.string = string
        self.newstr = newstr

    def lengthOfLongestSubstring(self):
        final_dict = {}
        if self.string == ' ':
            return 1
        for char in self.string:
            if char not in self.newstr:
                self.newstr += char
            else:
                final_dict.update({self.newstr: len(self.newstr)})
                self.newstr = ''
                if char not in self.newstr:
                    self.newstr += char
        
        max_str = ''
        temp_value = 0
        for key, value in final_dict.items():
            if value > temp_value:
                temp_value = value
                max_str = key

        return max_str


# obj1 = LongestSubstring('abcabcbb')
# obj2 = LongestSubstring('pwwkew')
# obj3 = LongestSubstring('bbbbb')
obj3 = LongestSubstring(' ')

# final_str1 = obj1.lengthOfLongestSubstring()
# final_str2 = obj2.lengthOfLongestSubstring()
# final_str3 = obj3.lengthOfLongestSubstring()
final_str3 = obj3.lengthOfLongestSubstring()

# print(final_str1)
# print(final_str2)
print(final_str3)
