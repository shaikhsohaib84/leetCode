s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
obj = {}

for k,v in enumerate(s):
    obj[k] = v
    
string = ''
for val in indices:
    string += obj.get(val)

print(string)