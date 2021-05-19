'''
list.sort() and sorted(list)

'''

list_1 = [2,4,5,9,3,1,7,8,]

def selection(l):
    begin = 0

    for i in range(len(l)):
        small_i = begin
        for j in range(begin,len(l)):
            if l[small_i]>l[j]:
                small_i = j
        l[begin],l[small_i] = l[small_i], l[begin]
        begin+=1
    print(l)

selection(list_1)