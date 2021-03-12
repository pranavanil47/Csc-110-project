import random

def random_output(lst):
    i = len(lst)
    string = ''
    while i >0:
        number = random.randint(0,len(lst)-1)
        string +=' '+ lst[number]
        lst.pop(number)
        i-=1
    
    print(string)

random_output(['1', '2', '3']) 


