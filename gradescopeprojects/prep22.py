def count_vowels(string,index_1,index_2):
    count = 0
    for i in range(index_1,index_2+1):
        if string[i] == 'a' or string[i] == 'e'or string[i] == 'i'or string[i] == 'o'\
            or string[i] == 'u':
            count+=1
    return count
    

