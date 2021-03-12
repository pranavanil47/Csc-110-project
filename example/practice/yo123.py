def list_even_string(string):
    word_list = string.split(' ')
    count=[]

    for i in range(0,len(word_list)):
        word = word_list[i]
        a = word_list.index(word)
        word_list.remove(word)
        count.append(a)
            

    print(word_list)
    print(count)
list_even_string('Hello, how are you? Hello, I am doing well. I am too!')