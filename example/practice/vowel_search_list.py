def count_vow(lst):
    i = 0
    
    count = []
    c =0
    while i <len(lst):
        phrase = lst[i]
        for n in range(0,len(phrase)):
            if phrase[n] == 'a' or phrase[n] == 'e' or phrase[n] == 'i' or \
                phrase[n] == 'o' or phrase[n] == 'u':
                c+=1
        count.append(c)
        c =0
        i+=1
    
    print(count)

count_vow(["Hello World", "What's up?", "3", '' , "To be or not to be"])