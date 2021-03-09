def get_score():
    grades_list =[]

    subjects = int(input('Enter the number of subjects to calculate the\
         average '))
    i =1
    while subjects>0 :
        scores = float(input('Enter scores for',str(i)+'st', 'subject; ' ))
        grades_list= grades_list.append(scores)
        subjects -=1
        i+=1
    return grades_list


