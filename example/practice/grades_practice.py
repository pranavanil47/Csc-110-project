def get_score():
    grades_list =[]

    subjects = int(input('Enter the number of subjects to calculate the\
         average '))
    i =1
    while subjects>0 :
        scores = float(input('Enter scores for',str(i)+'subject; ' )