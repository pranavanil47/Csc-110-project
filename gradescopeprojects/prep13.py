

def count_characters(string, alpha1, alpha2):
    i = 0
    count_alpha = 0
    
    while len(string) > i :
        if string[i] == alpha1 or string[i] == alpha2:
            count_alpha += 1
        i += 1
    
    alpha1_print = '\''+ alpha1 + '\''
    alpha2_print = '\''+ alpha2 + '\''
    string_print = '\''+ string + '\''
    print(alpha1_print, 'and', alpha2_print, 'appeared', count_alpha, 'times in the string', string_print)

     
