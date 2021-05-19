###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that reads a text file from the user and prints 
###              a graph of numberof small words, meduim words and large words, 
###              the number of capitilized word to non-carptilized and the number 
###              of puctuated words to non-punctuated. This program also prints 
###              out the most occured small word, meduim word and large word with
###              their numeber of occurances. The file is converted to list then
###              to a dictonary with the format{string:occurances}. This program
###              also shows the number of unique words.
###

  

from graphics import graphics

def split_file(file_name):
    '''
    This function reads the text file and then splits into a list of words then
    returns it.
    Parameters;
    file_name: This can be string of text file name (.txt).
    '''
    file_to_open = open(file_name,'r')
    string = ''
    for line in file_to_open:                           # This loop is making a long string.
        string += line
    
    word_list = string.split()
    return word_list
        
def dict_creation(word_list):
    '''
    This Fuction creates a dictionary with unique words as keys and its number of
    occurances as values and returns it.(ex. {word:occurance})
    Parameters;
    word_list: Can be any list of strings.
    '''
    dictionary = {}
    for element in word_list:                        #This loop is searching the word list and apppending
        if element not in dictionary:                # to the dictionary 
            count = per_word(element,word_list)
            dictionary[element] = count
    return dictionary

def per_word(word,word_list):
    '''
    This fuction searches the list for a particular string given by the user and 
    returns the number of occurances in that list.
    Parameters;
    word: This can be any string needed to search in the list.
    word_list: This can be any list where the word needed to be searched in. 
    '''
    count = 0
    for element in word_list:                     # This loop is for counting the number of occurances
        if element == word:                       # in the word_list.
            count += 1
    return count

def most_occurunce(word_count):
    '''
    This function reads the dictionary and then returns which small word occurs
    the most and the number of times it occurs, same for medium and , large word.
    Parameters;
    word_count: This can be any dictionary with the format {string:integer} 
    '''
    large_count = 0
    med_count = 0
    small_count = 0
    for key,value in word_count.items():             # this loop is to find the most small word,
        length = len(key)                            # medium word and large word occured.
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
    med_word = value_to_key(med_count,word_count)    ## Finding which word is associated to the 
    large_word = value_to_key(large_count,word_count)## the specific occurance.
    return small_word, small_count ,med_word, med_count,large_word, large_count

def value_to_key(number,word_count):
    '''
    This function returns the string with the help of number of occurances.
    Parameters;
    number: This can be any integer of occurances or the value in the dictionary.
    word_count: This can be any dictionary with the format {string:integer}.
    '''
    for key,value in word_count.items():                       # looping to find the key to specific 
        if value == number:                                    # nuumber of occurances.
            return key

def occurance_count(word_count):
    '''
    This function reads the dictionary and returns the number of occurances of 
    small words, medium words and large words.
    Parameters;
    word_count: This can be any dictionary with the format {string:integer}.
    '''
    unique_count = 0
    no_of_small_words = 0
    no_of_med_words = 0
    no_of_large_words = 0
    for key in word_count:                    ## looping to count number of small, medium and large words
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
    '''
    This function reads the dictionary and checks if the word is captilized or not,
    and does a count of both captilized and non captilized  words.
    Parameters;
    word_count: This can be any dictionary with the format {string:integer}.
    '''
    cap = 0
    no_cap = 0
    for key in word_count:                     ## looping to check if each key is captilized or not.
        if key[0].isupper() == True:
            cap+=1
        else:
            no_cap+=1
    return cap, no_cap

def punctuated_count(word_count):
    '''
    This function reads a dictionary and checks if the keys are punctuated,i.e.
    end with '.', ',', '?' or '!'. It returs the counts of number of punctuated 
    and non-punctuated.
    Parameters;
    word_count: This can be any dictionary with the format {string:integer}.
    '''
    punctuated = 0
    non_punctuated = 0
    
    for key in word_count:
        if key[-1] == '.' or key[-1] == '!' or key[-1] == '?' or key[-1] == ',':
            punctuated += 1                      ##looping through the dictionary to check for punctuation.
        else:
            non_punctuated += 1
    return punctuated, non_punctuated

def captilized_graph(PIXEL_CONSTANT,Y_CORDINATE_CONSTANT, WIDTH_CONSTANT, gui,\
    cap,no_cap,unique_count):
    '''
    This creates a bar graph of capitilize vs non-capitilized.
    Parameters;
    PIXEL_CONSTANT: This is an integer constant of the total size of the bar graph.
    Y_CORDINATE_CONSTANT: This is an integer contstant of where the bar graph will start.
    WIDTH_CONSTANT: This is an integer constant of the width of the bar graph.
    gui: Graphics user interface.
    cap:An integer of number of captilized words.
    no_cap: An integer of number of non-captilized words.
    unique_count: This is the number of unique words in the text file. 
    '''
    gui.text(270,Y_CORDINATE_CONSTANT-30,'CAP/Non-CAP','white',16)              ## Text
    gui.rectangle(270, Y_CORDINATE_CONSTANT, WIDTH_CONSTANT, \
        PIXEL_CONSTANT * (cap/unique_count),'cyan')                             ## cap rectangle
    
    gui.text(270,Y_CORDINATE_CONSTANT,'Captilized','black',10)
    new_y = Y_CORDINATE_CONSTANT+(PIXEL_CONSTANT*(cap/unique_count))
    gui.rectangle(270,new_y,150,PIXEL_CONSTANT*(no_cap/unique_count),'green')   ## non cap rectangle
    gui.text(270,new_y,'Non Captililzed','black',10)                            ## Text

def occurance_graph(gui,PIXEL_CONSTANT,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,\
    no_of_small_words,no_of_med_words,no_of_large_words,unique_count):
    '''
    This creates a bar graph of number of small words vs no of medium words vs no
    of large words.
    Parameters;
    PIXEL_CONSTANT: This is an integer constant of the total size of the bar graph.
    Y_CORDINATE_CONSTANT: This is an integer contstant of where the bar graph will start.
    WIDTH_CONSTANT: This is an integer constant of the width of the bar graph.
    gui: Graphics user interface.
    no_small_words: An integer of number of small words in the text.
    no_meed_words: An integer of number of meduim words in the text.
    no_large_words: An integer of number of large words in the text.
    unique_count: This is the number of unique words in the text file. 
    '''
    gui.text(100,Y_CORDINATE_CONSTANT-30,'Words Lengths','white',16)            ## Text
    gui.rectangle(100,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT*\
        (no_of_small_words/unique_count),'cyan')                                ## small  words rectangle
    
    gui.text(100,Y_CORDINATE_CONSTANT,'Small words','black',10)                 ## Text
    new_y_1 = Y_CORDINATE_CONSTANT+PIXEL_CONSTANT*(no_of_small_words/unique_count)
    
    gui.rectangle(100,new_y_1,WIDTH_CONSTANT,PIXEL_CONSTANT*(no_of_med_words/unique_count)\
        ,'green')                                                               ## medium words rectangele
    
    gui.text(100,new_y_1,'Medium words','black',10)                             ## Text
    new_y_2 = new_y_1 + PIXEL_CONSTANT*(no_of_med_words/unique_count)
    
    gui.rectangle(100,new_y_2,WIDTH_CONSTANT,PIXEL_CONSTANT*(no_of_large_words/unique_count)\
        ,'cyan')                                                                ## large words rectangle
    
    gui.text(100,new_y_2,'Large words','black',10)                              ## Text

def punctuated_graph(gui,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT,\
    punctuated, non_punctuated,unique_count):
    '''
    This creates a bar graph of punctuated vs non-punctuated
    Parameters;
    PIXEL_CONSTANT: This is an integer constant of the total size of the bar graph.
    Y_CORDINATE_CONSTANT: This is an integer contstant of where the bar graph will start.
    WIDTH_CONSTANT: This is an integer constant of the width of the bar graph.
    gui: Graphics user interface.
    punctuated:An integer of number of punctuated words.
    non_punctuated: An integer of number of non-punctuated words.
    unique_count: This is the number of unique words in the text file. 
    '''
    
    gui.text(450,Y_CORDINATE_CONSTANT-30,'Punct/Non-Punct','white',16)          ##Text
    gui.rectangle(450,Y_CORDINATE_CONSTANT,WIDTH_CONSTANT,PIXEL_CONSTANT*\
        (punctuated/unique_count),'cyan')                                       ##Punctuated rectangle
    
    gui.text(450,Y_CORDINATE_CONSTANT,'Punctuated words','black',10)            ##Text
    new_y_1 = Y_CORDINATE_CONSTANT+PIXEL_CONSTANT*(punctuated/unique_count)
    gui.rectangle(450,new_y_1,150,PIXEL_CONSTANT*(non_punctuated/unique_count),'green') ##Non-Punctuated rectangle
    gui.text(450,new_y_1,'Non Punctuated','black',10)                           ##Text  
    pass    

def bar_graph(word_count,file_name):
    '''
    This function creates the canvas for the the graphs, prints out the most occured
    small word, meduim word and large word and their number of occurances. This also
    prints the name of the text file read on the canvas and draws the three graphs
    number of occurnace graph, captilized and the punctuated graph.
    Parameters;
    word_count: This can be any dictionary with the format {string:integer}.
    file_name: This can be string of text file name (.txt).
    '''
    smlest_wrd,smlest_wrd_count, median_word, median_word_count, \
        largest_word, largest_word_count = most_occurunce(word_count)           ## all the variables
                                                                                ## for the overhead text
    unique_count, no_of_small_words, no_of_med_words, no_of_large_words = \
         occurance_count(word_count)                                            ## all of the variables for 
                                                                                ## the graphs
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
            str(largest_word_count)+'x)'                                        ## This is the overhead text
    
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