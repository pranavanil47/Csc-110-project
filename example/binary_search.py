items = [1,2,3,4,5,6,7,8,9,10]
def binary_search(l,x):
    sorted(l)
    first = 0
    last = len(l) -1

    while first < last:
        check = (first+last)//2
        if l[check] == x:
            return True
        elif l[check] < x:
            first = check+1
        else:
            last = check - 1
    return False

print(binary_search(items, 1))