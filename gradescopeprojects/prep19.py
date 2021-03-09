def grade_info(grades):
    highest_grade = max(grades)
    lowest_grade = min(grades)

    count = 0.00
    for i in range(0,len(grades)):
        count+= grades[i]
    
    average = count/len(grades)

    
    return highest_grade, lowest_grade,average
    


    