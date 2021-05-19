def double(file_name, double_file_name):
    file_open = open(file_name, 'r')
    string = ''
    for line in file_open:
        line_list = line.split(' ')
        for i in line_list:
            string += i + ' ' + i + ' '
        string += '\n'
    
    file_write = open(double_file_name,'w')
    file_write.write(string)
    file_write.close()

            
double('text.txt', 'text1.txt')