###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that searches a puzzle for words from a text file and
###               prints out the locations of the words in the form of [column,row]
###               in the puzzle which is also in the text file form.    
### 

def load_dictionary(word_dictionary,word_file):
    '''
    This function is use to open the text file containing the words search list
    and make a dictionary of those words.
    Parameters;
    word_dictionary: This is an empty dictionary used to store the words.
    word_file: This can be any text file with specific format(word : backwords) 

    '''
    file_name = open(word_file, 'r')

    for line in file_name:
        string = line.strip('\n')
        split_list = string.split(' ')
        word = split_list[0]
        reverse_word = split_list[2]

        word_dictionary[word] = reverse_word 

def check(line,word,reverse):
    '''
    This function checks whether the required word is in the row.
    Parameters;
    line: This is a string of the combined letters of one row in the grid.
    word: This is a string of the word needed to be searched in the row.
    reverse: This is a string of the backwards word needed to be searched in the row.

    '''

    if word in line or reverse in line:
        return True
    else:
        return False

def horizontal_mode_line(grid_list,word,reverse):
    '''
    This function checks each row to search if the words in the dictionary is found
    in the grid horizontally, if found it returs the position as columns,row
    Parameters;
    grid_list: This is list of all the rows in the grid file.
    word: This is a string of the word needed to be searched in the row.
    reverse: This is a string of the backwards word needed to be searched in the row.

    '''
    i = 0
    column = 0 
    line_req = ''
    while i <len(grid_list):
        string = grid_list[i]
        line_list = string.split(' ')

        line = ''.join(line_list)

        check_line = check(line,word,reverse)
        if check_line == True:
            column = i + 1
            line_req += line                 
        i+=1
    
    l = 0
    row = 0
    while l<len(line_req):
        if word[0] == line_req[l]:
            row += l
            l = len(line_req)
        l+=1
    return column,(row+1) 
            


def horizontal_mode(grid_file,word_dictionary):
    '''
    This function opens the grid file and coverts it into a list of strings, checks
    if each word in the dictionary word_dictionary is there in the the grid and if found 
    horizontally prints out its location in the grid.
    Parameters;
    grid_file: This is a text file (.txt) containing the puzzle or grid to be searched in. 
    word_dictionary: This is the dictionary of words required to be searched.

    '''
    file_open = open(grid_file, 'r')
    y_list = []
    for line in file_open:
        word = line.strip('\n')
        word = word.lower()
        y_list.append(word)
    
    for word,reverse in word_dictionary.items():
        column,row= horizontal_mode_line(y_list,word,reverse)
        if column != 0 and row != 0: 
            print(word, 'found at', '['+str(column)+', '+str(row)+']')




def main():
    word_file = input('Enter word file:\n')
    grid_file = input('Enter puzzle file:\n')
    mode = input('Enter puzzle mode:\n')
    word_dictionary = {}
    load_dictionary(word_dictionary,word_file)
    if mode == 'h':
        horizontal_mode(grid_file,word_dictionary)
    else:
        print('I didn\'t get time to complete vertical')

main()

        