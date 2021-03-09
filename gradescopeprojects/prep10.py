import os 

string =  input('Enter string:\n')
end_parenthesis = ')'
start_paranthesis = '('
index = 0 
end_parenthesis_count = 0
start_paranthesis_count= 0

while index < len(string) and start_paranthesis_count >= end_parenthesis_count :
    if string[index] == end_parenthesis:
        index += 1
        end_parenthesis_count += 1
    elif string[index] == start_paranthesis:
        index += 1
        start_paranthesis_count+=1
    else:
        index += 1
        
if start_paranthesis_count == end_parenthesis_count:
    print('Parentheses balanced') 

else:
    print('Parentheses unbalanced')

os._exit

#5 + (4 * (3 + (5 + 5)))