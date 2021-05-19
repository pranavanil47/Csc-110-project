a = {10,30,40,50}
b = {5,20,15,30,25,40}

c = a.intersection(b)

print(c)

d = {5,6,7,8}
e = {7,8,9,10}

f = d.issubset(b)
g = d.issuperset(b)

h = f and g
print(h)