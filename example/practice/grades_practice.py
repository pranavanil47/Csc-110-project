def get_score():
    grades_list =[]

    subjects = int(input('Enter the number of subjects to calculate the average '\
        ))
    
    while subjects>0:
        scores = int(input('Enter scores for subject: ' ))
        grades_list.append(scores)
        subjects-=1
    
    return grades_list

def kick_out_min():
    g= get_score()
    minimum_score = min(g)
    g.remove(minimum_score)
    return g,len(g)

def calculate_average():
    grades,subjects = kick_out_min()
    count = 0
    for i in range(0,len(grades)):
        count+= grades[i]
    
    average = count/subjects

    return average

def main():
    a= calculate_average()
    print('---------------------------------------')
    print('|   So your score average is ', a,'  |')
    print('---------------------------------------')
    

main()
