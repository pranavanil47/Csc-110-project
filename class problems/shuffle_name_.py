name = input('Enter a name:\n')

if name.isalpha():
    name = name.upper()
    print(name)

    i = 0 

    while i < len(name):
        last = name[-1]
        name = name[:-1]
        name = last + name
        print(name)
        i += 1
        

        