import string

input_str = '20 5 19 20+4 15 13 5' # TEST DOME

class numToStr():
    def __init__(self):
        self.num_str = ''
        self.alphabet_dict = {}
        self.alphabet = string.ascii_lowercase 
        # same thing in java-script
        # const arr = [...Array(26)].map((_, i) => String.fromCharCode(i + 97))

        
    # generate alphabet
    def generate_alphabet(self):
        for idx, char in enumerate(self.alphabet):
            self.alphabet_dict[str(idx+1)] = char
        
    def convert_to_str(self, string):
        for char in string.split(' '):
            char_num = self.alphabet_dict.get(char)
            if char_num:
                self.num_str += char_num
        self.num_str += ' '
            
        
    def num_to_str(self, string):
        self.generate_alphabet()
        arr = string.split('+')
        for num_char in arr:
            self.convert_to_str(num_char)
        return self.num_str.upper()
    
obj = numToStr()
print(obj.num_to_str(input_str))