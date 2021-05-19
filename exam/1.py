strings = [ ['jim', 'janet', 'innovate'],
            ['imitate', 'rifle', 'pizza'],
            ['rudimentary']]


def most_leters(list_name, letter):
    count_letter = 0
    for element_list in list_name:
        for i in element_list:
            list_letter_count = 0
            for j in range(len(i)):
                if i[j] == letter:
                    list_letter_count+=1
            if list_letter_count > count_letter:
                count_letter = list_letter_count
    return count_letter

print(most_leters(strings, 'i'))