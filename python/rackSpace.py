'''
    Given a string A and a dictionary of words B, determine if A can be segmented into a space- separated sequence of one or more dictionary words.

    ** Input Format ** 
    The first argument is a string, A.
    The second argument is an array of strings, B. 
    
    ** Output Format ** 
    Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

    ** Examples **
    Input 1:
        A = "myinterviewtrainer",
        B = ["trainer", "my", "interview"]
        Output => 1
    
    Input 2:
        A = "a"
        B = ["aaa"]
        Output => 0
'''
input_str_one = "myinterviewtrainer"
input_str_list_one = ["trainer", "my", "interview"]

input_str_two = "a"
input_str_list_two = ["aaa"]

class RackSpace:
    def __init__(self, input_string, input_list):
        self.input_string = input_string
        self.input_list = input_list

    def checkString(self):
        for string in self.input_list:
            status = 1 if string in self.input_string else 0
        return status


rs_obj_one = RackSpace(input_str_one, input_str_list_one)
rs_obj_two = RackSpace(input_str_two, input_str_list_two)

print(rs_obj_one.checkString())
print(rs_obj_two.checkString())