class Solution:
    def palindrome(self, str):
        n = len(str)

        if not n:
            return False
        elif n == 1:
            return str
        else:
            max_palindrome_size = 0
            max_palindrome_lst = []

            for i in range(0, n):
                i_str = str[i]
                for j in range(1, n):
                    i_str += str[j]
                    # sub_str = f'{str[i]}{str[j]}'
                    palin_str = i_str[::-1]

                    if i_str == palin_str:
                        max_palindrome_lst.append(i_str)
            
            return max_palindrome_lst

            

input_str = 'babad'
obj = Solution()
print(obj.palindrome(input_str))