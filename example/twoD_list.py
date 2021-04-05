items = [[9,8,7,8],
         [10,20,30,4],
         [5,10,55,4]

]

for i in items:
    for j in i:
        print(str(j)+'\t',end='')
    print()

for i in range(len(items)):
    for j in range(len(items))