def split_file(index_file,encrypted_file):
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

def decrypted_file(file_name,string):
    file = open(file_name, 'w')
    file.write(string)
    file.close()
    

    
def main():
    key,list_to_decrypt= split_file('index.txt','encrypt.txt')
    decrypted_string = decrypter(key,list_to_decrypt)
    decrypted_file('encrypt.txt',decrypted_string)
    

main()