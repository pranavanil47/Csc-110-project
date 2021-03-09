
def tax_print(salary):
    if salary < 10000:
        print('taxe are', (salary * 0.15))

    elif salary < 50000:
        print('taxe are', (salary * 0.20))
    elif salary < 150000:
        print('taxe are', (salary * 0.30))


index = 3
while index > 0:
    money = int(input('Enter your salary'))
    tax_print(money)
    index -= 1