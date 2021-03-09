'''
this is a program that asks iput from user and prints out the summary of weekend 
(without return function)
'''


import os 

print('-----Weekend planner-----')
print()

tasks = '+----------------+\n+---  Weekend Summary -----+\n-----------------+\n'

def input_day(day):
    print('----'+ day +'----')
    global tasks
    task= '' 
    tasks += '---------'+ day +'-------\n'

    while task != 'sleep':
        task = input('Next task for ' + day + ': ')
        tasks += ' * ' + task + '\n'
    print()
      
def main():
    input_day('Friday')
    input_day('Saturday')
    input_day('Sunday')
    print(tasks)

main()

    

    
