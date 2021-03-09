def get_score():
    grades_list =[0]

    subjects = int(input('Enter the number of subjects to calculate the average '\
        ))
    
    while subjects>0:
        scores = int(input('Enter scores for', 'subject: ' ))
        
        subjects-=1
    

    return grades_list ,scores

def main():
    print(get_score())
    

main()
