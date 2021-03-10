
def get_sales():
    sale =[]
    days = ['Sunday', 'Monday','Tuesday' ,'Wednesday','Thursday','Friday',\
        'Saturday']
    i =1
    d =0
    while i<=7:
        sales_input = float(input('Enter the amount on '+days[d]+ ' '))
        sale.append(sales_input)
        i+=1
        d+=1
    return sale

def main():
    sale = get_sales()
    count = 0.00
    for i in range(0,len(sale)):
        count+=  sale[i]
    print()
    print('---------------------------------')
    print('Your sale f0r this week is',count)
    print('---------------------------------')

main()