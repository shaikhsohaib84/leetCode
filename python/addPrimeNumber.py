

def checkPos(self, char):
    for row in range(self.start, self.array_row):
        try:
            col_indx = self.array[row].index(char)
            if col_indx:
                self.get_next_string()

            return [row, col_indx]
        except:
            
            return [None, None]
            
def mainFunc(self):
    
    while self.char_pos < self.max_string_len:
        pos_lst = self.checkPos(self.string[self.char_pos])
        
        if all(pos_lst):
            pass


            
        
obj = findArray()
obj.mainFunc()


a = ['a', 'b', 'c']

while (a.pop())