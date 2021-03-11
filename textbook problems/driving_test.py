def correct_answers():
    string = 'A C A A D B C A C B '
    correct = string.split(' ')
    return correct
def student_input():
    i =1
    string = ''
    while i<=10:
        a = input('Enter The anwer for question(A,B,C,D) '+str(i)+ ' ')
        a = a.upper()
        string+= ' '+ a
        i+=1
    input('Enter to save your answers...........')
    print()
    answers = string.split(' ')
    answers =answers[1:]
    
    return answers



def main():
    correct =correct_answers()
    student = student_input()
    i = 0
    score = 0
    while i<5:
        if correct[i] == student[i]:
            score+=1
        i+=1
    input('Press Enter your score...........')
    print('------------------------------------------------')
    if score >= 5:
        print('Your score is', score)
        print('Congrats, You have passed')
    else:
        print('Your score is', score)
        print('Sorry you failed, Better luck next time ')
    print('------------------------------------------------') 



main()