'''
This program makes a odd number in a list and make it even
'''
weights = [150,137,187,175,170,150,129]

def make_even(w):
    i =0 
    while i < len(w):
        if w[i]%2 != 0:
            w[i] += 1
        i+=1
    return w

print(make_even(weights))
