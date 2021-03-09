def get_score():
    grades_list =[]

    subjects = int(input('Enter the number of subjects to calculate the average '\
        ))
    
    i =1
    while i <= subjects:
        scores = int(input('Enter scores for', 'subject; ' ))
        grades_list= grades_list.append(scores)
        
        i+=1
    return grades_list


def main():
    a = get_score()
    print(a)

main()