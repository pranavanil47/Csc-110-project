list_1 = [2,3,4,6,1,5,7,9,8]

def buble_sort(l):
    end = len(l)

    for i in range(len(l)):
        for j in range(end-1):
            if l[j]>l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
        end -= 1
    print(l)

buble_sort(list_1)

