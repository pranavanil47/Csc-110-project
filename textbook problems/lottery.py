import random

def random_generator():
    number= random.randint(0,9)

    return number

def list_generator():
    lotery_list = []
    i = 0
    while i<7:
        number = random_generator()
        lotery_list.append(number)
        i+=1

    return lotery_list

def print_winner():
    winner = list_generator()
    string= ''
    for i in range(0,len(winner)):
        string += str(winner[i])
    
    print('The winning lottery is')
    input('Press Enter to find out.............')
    print(string)
    

def main():
    
    print_winner()


main()

