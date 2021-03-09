name = input('Enter ur name')

def cap(name_print):
    global name
    first_letter = name[0].upper
    after_first = name[:1].lower
    name_print = first_letter + after_first
    return name_print



