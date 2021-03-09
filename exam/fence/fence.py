string = input('characters for fence posts:\n')

i = 0 
string_coint= ''
while i < len(string):
    a = ('--'+ string[i]+'--')
    i += 1
    string_coint += a
    
 

print (string_coint)