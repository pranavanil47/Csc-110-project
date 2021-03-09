'''
same as weekend planer.py but wit the return function
'''


import os 

print('-----Weekend planner-----')
print()



def input_day(day):
    print('----'+ day +'----')
    tasks = ''
    task= '' 
    tasks += '---------'+ day +'-------\n'

    while task != 'sleep':
        task = input('Next task for ' + day + ': ')
        tasks += ' * ' + task + '\n'
    return tasks    
    print()
      
def main():
    fr = input_day('Friday')
    sat = input_day('Saturday')
    sund = input_day('Sunday')
    print('===========\n    weekend summary    \n============')
    print(fr)
    print(sat)
    print(sund)
   

main()
    
    

    
