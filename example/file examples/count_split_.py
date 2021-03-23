def most_used_char(string):
    most_count = 0
    most_letter = ''

    for c in string:
        if string.count(c)>most_count:
            most_count = string.count(c)
            most_letter = c
    return most_letter

print(most_used_char('Hellokkkkkkkkkk there'))

def swap_words(string, word1, word2):
    string_list = string.split(' ')
    for i in range(len(string_list)):
        if string_list[i] == word1:
            string_list[i] = word2
        elif string_list[i] == word2:
            string_list[i] = word1
    final_output = ' '.join(string_list)
    return(final_output)
def get_index()
print(swap_words('Hi how are you', 'you', 'Hi'))