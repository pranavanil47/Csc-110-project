def get_file(list_name):
    file_open = open('puzzle.txt','r')
    for line in file_open:
        word = line.strip('\n')
        list_name.append(word)
    
def reverse(word):
    i = 1
    reverse = ''
    while i<(len(word)+1):
        last_letter = word[-i]
        reverse+=last_letter
        i+=1
    return reverse

def reverse_list_function(list_words,reverse_list):
    for word in list_words:
        reverse_word = reverse(word)
        reverse_list.append(reverse_word)

     

def write_text(list_words,reverse_list):
    file_name = open('words.txt','w')
    to_write = ''
    i = 0
    while i <len(list_words):
        words = list_words[i]
        reverse_words = reverse_list[i]
        line = words +' : '+ reverse_words + '\n'
        to_write += line
        i+=1
    file_name.write(to_write)
    file_name.close()
        
    
       
    
    #file_name.close()


def main():
    list_words = []
    reverse_list = []
    get_file(list_words)
    reverse_list_function(list_words,reverse_list)
    write_text(list_words,reverse_list)



main()