import os
week  = int(input('how many weeks of work'))
total_pay = 0
total_hours= 0

index = 0
while index < week:
    pay = int(input('week ' + str(index +1) + ' pay'))
    hours = int(input('week ' + str(index +1) + ' hour'))
    total_pay += pay
    total_hours += hours
    index+= 1

avg_weekly_pay = total_pay / week
avg_hourly_pay = total_pay/ total_hours

print('------')
print('ur avg weekly wage is $'+ format(avg_weekly_pay, ',.2f'))
print('ur avg hourly wage is $'+ format(avg_hourly_pay, ',.2f') + ' per hour')