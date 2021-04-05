csv_data = []

csv_file = open('numbers.csv', 'r')

for line in csv_file:
    line = line.strip('\n')
    values = line.split(',')
    num_values = []
    for i in values:
        num_values.append(int(i))
    csv_data.append(num_values)

print(csv_data)

flipped  = []

for i in csv_data:
    flipped.insert(0,i)

for i in flipped:
    for j in i:
        print(str(j) +', ',end='')
    print()
    

