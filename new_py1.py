# 1. Convert a string of numbers to a sentence. Each number represents a letter. Numbers in the string are separated by a space and words in the sentence are separated by a plus character. 
# Conversion table : 

# A=1
# B=2
# C=3
# D=4
# .......
# Z=26.
# Example: numbers_to_letters("20 5 19 20+4 15 13 5") should return "TEST DOME".


aplha_dict = {
    1: 'a',
    2 :'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g', 
    8: 'h', 
    9:'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15:'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24:'x',
    25:'y',
    26:'z'
}

def num_to_letter(string):
    str_lst = string.split()
    return_str = ''
    for char in str_lst:
        if '+' in char:
            temp = char.split('+')
            
            if aplha_dict.get(int(temp[0])):
                return_str += aplha_dict.get(int(temp[0]))
                return_str += ' '
            
            return_str += aplha_dict.get(int(temp[1]))
            continue

        if aplha_dict.get(int(char)): 
            return_str += aplha_dict.get(int(char))
    return return_str.upper()

    # for char in string:


input = "20 5 19 20+4 15 13 5" 
res = num_to_letter(input)
print(res)













# You have three tables Teacher(id,name), Subject(id,name) and TeacherSubject(id,teacher_id, subject_id). 
# In TeacherSubject table (teacher_id,subject_id) will be unique. 
# You need to create a SQL/ORM query which will return the total number of subjects for given teacher id.

# TeacherSubject.objects.filter(teacher_id = 4).count()

# TeacherSubject.objects.filter(teacher_id = 4).values('subject_id').count()

