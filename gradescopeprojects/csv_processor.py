###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that reads a csv file and then does any of the three
###               operations; maximum, minimum and average of a column.   
###                
###
def read_file(file_name,number_list):
    '''
    This function reads the csv file and converts the numbers in the csv into a
    two D list of rows.
    Parameters;
    file_name: Can be string of the name of the csv required.
    number__list: An empty list in which the 2D list of rows are stored.  
    '''
    file_open = open(file_name,'r')
    for line in file_open:
        line = line.strip('\n')
        row_split = line.split(',')
        number_list.append(row_split)
    
def column_list(list_name):
    '''
    This function colverts the 2D list of rows into a 2D list of columns and 
    returns it.
    Parameters;
    list_name: This can be a 2D list.
    '''
    list_coloumn = [] 
    length = len(list_name[0])
    number = 0
    while number < length:
        colomn = column_list_converter(list_name,number)
        list_coloumn.append(colomn)
        number+=1
    return list_coloumn

def column_list_converter(list_name,number):
    '''
    This function makes a new 1D list of numbers from a specific index of f from
    an existing 2D list. 
    '''
    colom = []
    for element in list_name:
        add_number = float(element[number])
        colom.append(add_number)
    
    return colom

def commands(command,colmn,colmn_number):
    '''
    This fucnction gives the desired output according to the command given by the
    user.
    Parameters;
    command: This can be any of these string 'avg','max' or 'min'.
    colomn: This is the column list where the operation is done.
    colomn_number: This a integer which is the column number where the operation
                   is done 
    '''
    if command =='avg':
        average_calculate(colmn,colmn_number)
    elif command =='min':
        minimum(colmn,colmn_number)
    elif command =='max':
        maximum(colmn,colmn_number)

def average_calculate(colmn,colmn_number):
    '''
    This function calculates the average and prints it out from the column list.
    Parameters;
    colomn: This is the column list where the operation is done.
    colomn_number: This a integer which is the column number where the operation
                   is done 
    '''
    i = 0
    count = 0
    while i < len(colmn):
        count += colmn[i]
        i +=1
    average = count/len(colmn)
    print('The average for column', colmn_number, 'is:', average)

def minimum(colmn,colmn_number):
    '''
    This function calculates the minimum and prints it out from the column list.
    Parameters;
    colomn: This is the column list where the operation is done.
    colomn_number: This a integer which is the column number where the operation
                   is done 
    '''
    mini = 100000000000.0
    for element in colmn:
        if element < mini:
            mini = element
    print('The minimum value in column', colmn_number, 'is:', mini)


def maximum(colmn,colmn_number):
    '''
    This function calculates the average and prints it out from the column list.
    Parameters;
    colomn: This is the column list where the operation is done.
    colomn_number: This a integer which is the column number where the operation
                   is done 
    '''
    maxi = 0.0
    for element in colmn:
        if element>maxi:
            maxi = element
    print('The maximum value in column', colmn_number, 'is:',maxi)


def main():
    file_to_read = input('Enter CSV file name:\n')
    colmn_number =int(input('Enter column number:\n'))
    coloumn_to_calculate = colmn_number - 1
    command = input('Enter column operation:\n')
    number_list = []
    read_file(file_to_read,number_list)
    list_col = column_list(number_list)
    colmn = list_col[coloumn_to_calculate]
    commands(command,colmn,colmn_number)

    

main()

       
    