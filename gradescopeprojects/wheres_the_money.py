###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that prints that helps a user visualize and understand how much money they spend of 
###               various categories of expenditures on the following input; Salary,food,rent,travel and bills   
###



import os

print('-----------------------------')
print('----- WHERE\'S THE MONEY -----')
print('-----------------------------')
sal1 =input('What is your annual salary?\n') # sal = salary input
if sal1.isnumeric() == False or int(sal1)<0:
    print('Must enter positive integer for salary.')
    os._exit(0)
elif sal1.isnumeric() == True or int(sal1)>0:
    sal = int(sal1)

mr1 =input('How much is your monthly mortgage or rent?\n') # mr = monthly rent input
if mr1.isnumeric() == False or int(mr1)<0:
    print('Must enter positive integer for mortgage or rent.')
    os._exit(0)
elif mr1.isnumeric() == True and int(mr1)>0:
    mr = int(mr1)
 
mb1 =input('What do you spend on bills monthly?\n') # mb = monthly bills input
if mb1.isnumeric() == False or int(mb1)<0:
    print('Must enter positive integer for bills.')
    os._exit(0)
elif mb1.isnumeric() == True and int(mb1)>0:
    mb = int(mb1)

wg1 =input('What are your weekly grocery/food expenses?\n') # wg = weekly groceries input
if wg1.isnumeric() == False or int(wg1)<0:
    print('Must enter positive integer for food.')
    os._exit(0)
elif wg1.isnumeric() == True and int(wg1)>0:
    wg = int(wg1)

trl1 =input('How much do you spend on travel annually?\n')  # annual travel input
if trl1.isnumeric() == False or int(trl1)<0:
    print('Must enter positive integer for travel.')
    os._exit(0)
elif trl1.isnumeric() == True and int(trl1)>0:
    trl = int(trl1)
    
if 0 <= sal <= 15000:
    tax = int(sal *(10/100))
if 15000 < sal <= 75000:                            ## calculating the tax based on the salary input
    tax = int(sal *(20/100))
if 75000 < sal <=200000:
    tax = int(sal *(25/100))
if sal > 200000:
    tax = int(sal *(30/100))

rent_annual = mr * 12
bill_annual = mb * 12                            # annual cost of all the input
food_annual = wg * 52
travel_annual = trl
if tax<75000:
    extra = (sal - (rent_annual+tax+bill_annual+food_annual+travel_annual))        #cappin the tax  

if tax >=75000:
    extra = (sal - (rent_annual+75000+bill_annual+food_annual+travel_annual))         #cappin the tax
    


tax_print = (format(tax, '11,.2f'))                                        ### formating to string
rent_annual_print = format(rent_annual, '11,.2f')                          ### formating to string
bill_annual_print = format(bill_annual, '11,.2f')                          ### formating to string
food_annual_print = format(food_annual, '11,.2f')                          ### formating to string
travel_annual_print = format(travel_annual, '11,.2f')                       ### formating to string
extra_print = format(extra, '11,.2f')                                       ### formating to string

tax_per=float((tax/sal) * 100)                                                 ## converting it to percentage of the tax
rent_annual_per =float((rent_annual/sal) * 100)                                ## converting it to percentage of the tax
bill_annual_per = float((bill_annual/sal) * 100)                               ## converting it to percentage of the tax
food_annual_per = float((food_annual/sal) * 100)                               ## converting it to percentage of the tax
travel_annual_per =float((travel_annual/sal) * 100)                            ## converting it to percentage of the tax
extra_per = float((extra/sal) * 100)

tax_per_print = format(tax_per, '6,.1f')                                       ## formating the percentages to string
bill_annual_per_print = format(bill_annual_per, '6,.1f')                       ## formating the percentages to string
food_annual_per_print = format(food_annual_per, '6,.1f')                       ## formating the percentages to string
travel_annual_per_print = format(travel_annual_per, '6,.1f')                   ## formating the percentages to string
extra_per_print = format(extra_per, '6,.1f')                                   ## formating the percentages to string
rent_annual_per_print = format(rent_annual_per, '6,.1f')                        ## formating the percentages to string

z = max(int(tax_per),int(bill_annual_per),int(rent_annual_per),int(food_annual_per),int(travel_annual_per),int(extra_per))
print(' ')
print('------------------------------------------'+ '-'*z)
print('See the financial breakdown below, based on a salary of $'+format(sal, '.0f'))
print('------------------------------------------'+'-'*z)
print('| mortgage/rent | $'+rent_annual_print+' |'+rent_annual_per_print+'% | '+'#' * int(rent_annual_per) )
print('|         bills | $'+bill_annual_print+' |'+bill_annual_per_print+'% | ' +'#' * int(bill_annual_per))
print('|          food | $'+food_annual_print+' |'+ food_annual_per_print+'% | '+'#' * int(food_annual_per))
print('|        travel | $'+travel_annual_print+' |'+travel_annual_per_print+'% | '+ '#' * int(travel_annual_per))
if tax < 75000:
    print('|           tax | $' + tax_print+' |'+tax_per_print+'% | '+ '#' * int(tax_per))
elif tax >= 75000:
    print('|           tax | $' +'  75,000.00'+' |'+format((float((75000/sal)*100)),'6,.1f' )+'% | '+ '#' *int( (75000/sal)*100))

print('|         extra | $'+ extra_print+' |'+extra_per_print+'% | '+ '#' * int(extra_per) )
print('------------------------------------------'+'-'*z)
if tax >= 75000:
    print('>>> TAX LIMIT REACHED <<<')

elif tax < 75000:
    os._exit

if extra < 0:
    print('>>> WARNING: DEFICIT <<<')
elif extra >= 0:
    os._exit
else:
    os._exit