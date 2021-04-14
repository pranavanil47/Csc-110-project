def calories(file_name):
    file_to_open = open(file_name, 'r')
    calorie_dict = {}
    for line in file_to_open:
        print(line)
        line.strip('\n')
        string_split = line.split(',')
        print(string_split)
        calorie_dict[string_split[0]] = string_split[1]
    
    #calorie_dict['name']
    low_count  = 0
    good_count = 0
    high_count = 0

    for key,value in calorie_dict.items():
        if value >2500:
            high_count+=1
        elif value<2000:
            low_count+=1
        else:
            good_count+=1
    
    print('low:', low_count)
    print('good:', good_count)
    print('high:', high_count)

calories('calories.csv')