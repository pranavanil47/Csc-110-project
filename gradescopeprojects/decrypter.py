###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that decrypts an encrypted text file with the help 
###               of an idex file or a key and saves as a text file.    
### 


def split_file(index_file,encrypted_file):
    '''
    This function splits the contents of the text file and the index file into a
    list and returns it.
    Parameters;
    encrypted_file: A string contiaining .txt file to decrypt.
    index_file: A string containing .txt file used as the key to decrypt. 
    '''
    index_list = []
    file_index = open(index_file, 'r')
    line_index = file_index.readlines()
    for line in line_index:
        p = int(line[:-1])-1
        index_list.append(p)
    
    string_list =[]
    string = open(encrypted_file, 'a')
    string.write(' ')
    string.close()
    string = open(encrypted_file, 'r') 
    string_line = string.readlines()
    for line in string_line:
        p = line[:-1]
        string_list.append(p)
    
    return index_list, string_list
  
def decrypter(key,list_to_decrypt):
    '''
    This function rearanges the string list into the correct order with respect 
    to the index list provided and returns the string with correct order.
    Parameters;
    key: Can be a list of integers.
    list_to_decrypt: Can be a list of strings.
    '''
    decrypted_list=[''] * len(key)
    
    i = 0
    while i <len(key):
        index = key[i]
        decrypted_list[index] = list_to_decrypt[i]
        i+=1
    string = '\n'.join(decrypted_list)
    return string 

def decrypted_file(string):
    '''
    This function makes a new text file named decrypted.txt containing the decrypted
    message or the orginal text file.
    Parameters;
    string: Can be a string used to write into a new text file.
    '''
    file = open('decrypted.txt', 'w')
    file.write(string)
    file.close()
    

    
def main():
    file_name = input('Enter the name of an encrypted text file:\n')
    key = input('Enter the name of the encryption index file:\n')
    key,list_to_decrypt= split_file(key,file_name)
    decrypted_string = decrypter(key,list_to_decrypt)
    decrypted_file(decrypted_string)
    

main()