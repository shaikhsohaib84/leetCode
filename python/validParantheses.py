class ValidParantheses:
    def __init__(self, input_string=''):
        self.input_string = input_string
        self.stack = []
        self.para_dict = {
            # '(' : ')',
            # '[': ']',
            # '{': '}',
            ')': '(',
            ']': '[',
            '}': '{'
        }

    def validator_string(self):
        for char in self.input_string:
            last_char = len(self.stack)
            if last_char and self.para_dict.get(char, None) == self.stack[last_char-1]:
                self.stack.pop()
            else:
                self.stack.append(char)
        return True if not self.stack else False



input_string = "(){}}{"
# input_string = "()"
# input_string = '[(])'
obj = ValidParantheses(input_string)
print(obj.validator_string())
