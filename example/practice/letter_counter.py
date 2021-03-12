def letter_count(lst,let):
    string =''
    for i in range(len(lst)):
        string+= lst[i]
    count  = 0
    for k in range(len(string)):
        if string[k] == let:
            count+=1
    print('There are',count, let+'\'s in the string')

letter_count(['abcd', 'tree', 'tech'], 'e')