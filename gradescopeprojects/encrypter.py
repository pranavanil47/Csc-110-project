import random

def  split_file(file_to_encrypt):
    file_split = open(file_to_encrypt, 'a')
    list_words= []
    file_split.write(' ')
    file_split.close

    file_split = open(file_to_encrypt, 'r') 
    lines = file_split.readlines()
    for line in lines:
        p = line[:-1]
        list_words.append(p)
    
    return list_words

def get_index(list_words):
    index_list=[]
    i = 1
    while i<= len(list_words):
        index_list.append(i)
        i+=1
    
    for i in range(0, len(list_words)*5):
        a = random.randint(0,len(list_words)-1)
        b = random.randint(0,len(list_words)-1)
        temp = index_list[a]
        index_list[b] = index_list[a]
        index_list[a] = temp

    return index_list

def encrypt(index_list,words_list):
    i = 0
    shuffle_list= []
    while i <len(index_list):
        k = index_list[i] -1
        shuffle_list.append(words_list[k])
        i+=1
    
    string = '\n'.join(shuffle_list)
    
    return string
def encrypt_file(file_to_encrypt,encrypted_index,encrypted_string):
    index_file = open('index.txt', 'w')
    for i in range(len(encrypted_index)):
        k = str(encrypted_index[i])+'\n'
        index_file.write(k)
    index_file.close()

    encrypted_file = open(file_to_encrypt, 'w')
    encrypted_file.write(encrypted_string)
    encrypted_file.close() 


def main():
    random.seed(125)
    words_list = split_file('encrypt.txt')

    encrypted_index = get_index(words_list)
    print(encrypted_index)
    '''
    encrypted_string = encrypt(encrypted_index,words_list)
    encrypt_file('encrypt.txt',encrypted_index,encrypted_string)
    '''
main()

