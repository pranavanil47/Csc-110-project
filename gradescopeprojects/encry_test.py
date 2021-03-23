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
    list_words= list_words[:-1]
    return list_words

def get_index(list_words):
    index_list=[]
    count = 0
    i = 1
    r =0
    k = random.randint(1,len(list_words))
    while i<= len(list_words):
        k = random.randint(1,len(list_words))
        while r<i:
            if index_list[r] == k:
                count+=1
        if count == 0:
            index_list.append(k)
        i+=1
        r+=1
        count= 0 
     
    print(index_list)

        
    
    random.shuffle(index_list)
    print(index_list)

def main():
    random.seed(125)
    words_list = split_file('encrypt.txt')
    get_index(words_list)

    
main()

