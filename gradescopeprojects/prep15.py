def get_height_category(gender, height):
    if gender == 'female':
        if int(height) > 64:
            print_output = 'above average'
        else:
            print_output ='below average'
    elif gender == 'male':
        if int(height) > 70:
            print_output = 'above average'
        else:
            print_output ='below average'    
    else:
        print_output = 'unknown average'
    
    return print_output



