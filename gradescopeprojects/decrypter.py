def split_file(index_file,encrypted_file):
    '''
    This function splits the contents of the text file and the index file into a
    list and returns it.
    Parameters;
    encrypted_file: A string contiaining .txt file to decrypt.
    index_file: A string containing .txt file used as the key 
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
    decrypted_list=[''] * len(key)
    
    i = 0
    while i <len(key):
        index = key[i]
        decrypted_list[index] = list_to_decrypt[i]
        i+=1
    string = '\n'.join(decrypted_list)
    return string 

def decrypted_file(string):
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