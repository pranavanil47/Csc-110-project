def every_other(string):
    string_list = string.split(' ')
    other_list = []
    for i in range(len(string_list)):
        if i % 2 == 0:
            other_list.append(string_list[i])
    
    string = ' '.join(other_list)
    return string

