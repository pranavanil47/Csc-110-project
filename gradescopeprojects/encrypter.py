###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description :A program that decrypts a text file and also provides the key to
###              to decrypt it, saves both as a text file.
###
import random

def  split_file(file_to_encrypt):
    '''
    This function splits the contents of the text file into a list and returns it.
    Parameters;
    file_to_encrypt: A string containing a .txt file to encrypt.
    '''

    list_words= []
    
    file_split = open(file_to_encrypt, 'r') 
    lines = file_split.readlines()
    for line in lines:
        p = line[:-1]
        list_words.append(p)
    
    list_words[:-1]
    
    return list_words

def get_index(list_words):
    '''
    This function first makes an index list and shuffles it and returns the shuffled
    list.
    Parameter;
    list_words: This can be a list of strings. 
    '''
    index_list=[]
    i = 1
    while i<= len(list_words):
        index_list.append(i)
        i+=1
    
    for i in range(len(index_list)*5):
        number_1 = random.randint(0,len(index_list)-1)
        number_2 = random.randint(0,len(index_list)-1)
        index_list[number_1],index_list[number_2] =index_list[number_2],\
            index_list[number_1]


    return index_list

def encrypt(index_list,words_list):
    '''
    This function encrypts or shuffles the string list according to the shuffled
    index.
    Parameters;
    index_list: This can be a list of integers.
    words_list: this can be a list of strings 
    '''
    i = 0
    shuffle_list= []
    while i <len(index_list):
        k = index_list[i] -1
        shuffle_list.append(words_list[k])
        i+=1
    
    string = '\n'.join(shuffle_list) + '\n' + ' '
    
    return string

def encrypt_file(encrypted_index,encrypted_string):
    '''
    This function makes a new text file named encrypted.txt file needed to be 
    encrypted with the new shuffled string and also makes a new shuffled index 
    file as a text file named index.txt.
    Parameters;
    file_to_encrypt: A string containg a .txt file to encrypt.
    encrypted_index: This is the shuffled index list.
    encrypted_string: This is the shuffled string list.

    '''
    index_file = open('index.txt', 'w')
    for i in range(len(encrypted_index)):
        k = str(encrypted_index[i])+'\n'
        index_file.write(k)
    index_file.close()

    encrypted_file = open('encrypted.txt', 'w')
    encrypted_file.write(encrypted_string)
    encrypted_file.close() 


def main():
    random.seed(125)
    file_name = input('Enter a name of a text file to encrypt:\n')
    words_list = split_file(file_name)

    encrypted_index = get_index(words_list) 
    encrypted_string = encrypt(encrypted_index,words_list)
    encrypt_file(encrypted_index,encrypted_string)

main()
