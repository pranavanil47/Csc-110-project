def calories(file_name):
    file_to_open = open(file_name, 'r')
    calorie_dict = {}
    for line in file_to_open:       
        line = line.strip('\n')
        string_split = line.split(',')
        if string_split[1].isnumeric() == True:
            calorie_dict[string_split[0]] = int(string_split[1])
    

    low_count  = 0
    good_count = 0
    high_count = 0

    for key,value in calorie_dict.items():
        if value >2500:
            high_count+=1
        elif value<2000:
            low_count+=1
        elif 2000<= value <= 2500:
            good_count+=1
    
    print('low:', low_count)
    print('good:', good_count)
    print('high:', high_count)
    
    
    

    

calories('calories.csv')

