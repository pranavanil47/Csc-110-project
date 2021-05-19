list_1 = [2,3,4,6,1,5,7,9,8]

def inertion_sort(l):
    for compare_index in range(1, len(l)):
        ci = compare_index
        for j in range(ci-1, -1, -1):
            if ci<0 or l[ci]>= l[j]:
                break
        else:
            l[ci], l[j] = l[j], l[ci]
            ci -= 1
    print(l)

inertion_sort(list_1)
