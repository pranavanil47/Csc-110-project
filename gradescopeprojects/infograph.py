from graphics import graphics

def split_file(file_name):
    file_to_open = open(file_name,'r')
    string = ''
    for line in file_to_open:   
        string += line
    
    word_list = string.split()
    return word_list
        
def dict_creation(word_list):
    dictionary = {}
    for element in word_list:
        if element not in dictionary:
            count = per_word(element,word_list)
            dictionary[element] = count
    return dictionary

def per_word(word,word_list):
    count = 0
    for element in word_list:
        if element == word:
            count += 1
    return count

def most_occurunce(word_count):
    large_count = 0
    med_count = 0
    small_count = 0
    for key,value in word_count.items():
        length = len(key)
        if length <= 4:
            if value > small_count:
                small_count = value
        elif 5 <= length <=7:
            if value > med_count:
                med_count = value
        elif length >= 8:
            if value > large_count:
                large_count = value
    small_word = value_to_key(small_count,word_count)
    med_word = value_to_key(med_count,word_count)
    large_word = value_to_key(large_count,word_count)
    return small_word, small_count ,med_word, med_count,large_word, large_count

def value_to_key(number,word_count):
    for key,value in word_count.items():
        if value == number:
            return key

def occurance_count(word_count):
    unique_count = 0
    no_of_small_words = 0
    no_of_med_words = 0
    no_of_large_words = 0
    for key in word_count:
        length = len(key)
        if length <= 4:
            no_of_small_words+=1
        elif 5 <= length <=7:
            no_of_med_words+=1
        elif length >= 8:
            no_of_large_words+=1
        unique_count+=1
    return unique_count, no_of_small_words, no_of_med_words, no_of_large_words  

def capitalized_count(word_count):
    cap = 0
    no_cap = 0
    for key in word_count:
        if key[0].isupper() == True:
            cap+=1
        else:
            no_cap+=1
    return cap, no_cap

def punctuated_count(word_count):
    punctuated = 0
    non_punctuated = 0
    
    for key in word_count:
        if key[-1] == '.' or key[-1] == '!' or key[-1] == '?' or key[-1] == ',':
            punctuated += 1
        else:
            non_punctuated += 1
    return punctuated, non_punctuated

def captilized_graph(PIXEL_CONSTANT,Y_CORDINATE_CONSTANT, WIDTH_CONSTANT, gui,\
    cap,no_cap,unique_count):
    gui.text(270,Y_CORDINATE_CONSTANT-30,'CAP/Non-CAP','white',16)
    gui.rectangle(270, Y_CORDINATE_CONSTANT, WIDTH_CONSTANT, \
        PIXEL_CONSTANT * (cap/unique_count),'cyan')
    gui.text(270,Y_CORDINATE_CONSTANT,'Captilized','black',10)
    new_y = Y_CORDINATE_CONSTANT+(PIXEL_CONSTANT*(cap/unique_count))
    gui.rectangle(270,new_y,150,PIXEL_CONSTANT*(no_cap/unique_count),'green')
    gui.text(270,new_y,'Non Captililzed','black',10)

def occurance_graph(gui,PIXEL_CONSTANT,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,\
    no_of_small_words,no_of_med_words,no_of_large_words,unique_count):
    gui.text(100,Y_CORDINATE_CONSTANT-30,'Words Lengths','white',16)
    gui.rectangle(100,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT*\
        (no_of_small_words/unique_count),'cyan')
    gui.text(100,Y_CORDINATE_CONSTANT,'Small words','black',10)
    new_y_1 = Y_CORDINATE_CONSTANT+PIXEL_CONSTANT*(no_of_small_words/unique_count)
    gui.rectangle(100,new_y_1,WIDTH_CONSTANT,PIXEL_CONSTANT*(no_of_med_words/unique_count)\
        ,'green')
    gui.text(100,new_y_1,'Medium words','black',10)
    new_y_2 = new_y_1 + PIXEL_CONSTANT*(no_of_med_words/unique_count)
    gui.rectangle(100,new_y_2,WIDTH_CONSTANT,PIXEL_CONSTANT*(no_of_large_words/unique_count)\
        ,'cyan')
    gui.text(100,new_y_2,'Large words','black',10)
    pass

def punctuated_graph(gui,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT,\
    punctuated, non_punctuated,unique_count):
    gui.text(450,Y_CORDINATE_CONSTANT-30,'Punct/Non-Punct','white',16)
    gui.rectangle(450,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT*\
        (punctuated/unique_count),'cyan')
    gui.text(450,Y_CORDINATE_CONSTANT,'Punctuated words','black',10)
    new_y_1 = Y_CORDINATE_CONSTANT+PIXEL_CONSTANT*(punctuated/unique_count)
    gui.rectangle(450,new_y_1,150,PIXEL_CONSTANT*(non_punctuated/unique_count),'green')
    gui.text(450,new_y_1,'Non Punctuated','black',10)   
    pass    

def bar_graph(word_count,file_name):
    smlest_wrd,smlest_wrd_count, median_word, median_word_count, \
        largest_word, largest_word_count = most_occurunce(word_count)
    unique_count, no_of_small_words, no_of_med_words, no_of_large_words = \
         occurance_count(word_count)
    cap, no_cap = capitalized_count(word_count)
    punctuated, non_punctuated = punctuated_count(word_count)

    PIXEL_CONSTANT = 550
    Y_CORDINATE_CONSTANT = 190
    WIDTH_CONSTANT = 150

    gui = graphics(700, 750, 'Infograph')
    gui.rectangle(-10,-10,800,800,'grey')
    gui.text(50,50, file_name, 'cyan', 17)
    gui.text(50,80,'Total Unique Words: '+ str(unique_count),'white',19)
    
    occurance_string = smlest_wrd + ' ('+ str(smlest_wrd_count)+'x) ' + \
        median_word + ' ('+ str(median_word_count)+'x) '+ largest_word + ' ('+ \
            str(largest_word_count)+'x)'
    
    gui.text(50,110, 'Most used words(s/m/l): ','white',15)
    gui.text(270,110,occurance_string,'cyan',15)

    captilized_graph(PIXEL_CONSTANT,Y_CORDINATE_CONSTANT, \
        WIDTH_CONSTANT, gui,cap,no_cap,unique_count)
    occurance_graph(gui,PIXEL_CONSTANT,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,\
        no_of_small_words,no_of_med_words,no_of_large_words,unique_count)
    punctuated_graph(gui,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT,\
    punctuated, non_punctuated,unique_count)
    gui.primary.mainloop()

def main():
    file_name = input('Enter file name\n')
    word_list = split_file(file_name)
    word_count = dict_creation(word_list)
    bar_graph(word_count,file_name)

main()