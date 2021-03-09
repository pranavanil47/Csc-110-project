'''
This program searches for in the provided list from 
the input given by the user
'''

def main():
    product_list = ['VS234', 'VRRG475', 'TT83', 'WER845', 'EFR6773']

    search = input('Enter product number to search in database')

    if search in product_list:
        print(search, 'was found in database')
    else:
        print(search, 'was not found in database')

main()