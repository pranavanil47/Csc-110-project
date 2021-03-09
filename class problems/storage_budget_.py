### the goal is to write a program that accepts several inputs and determine how much RAM vs hard-drive storage a person can afford to purchase. The two inputs are

#●	The monetary budget (in dollars)
#●	Ther percentage of the budget that is for non-volatile storage (HDD/SSD)


budget = float(input('Computer Storage budget:  '))

per = float(input('%' + 'of non-volatile (long-term) storage: '))

cost_hdd_ = 0.50 
cost_ram_ = 10.00 

amnt_budget_ram_ = budget * (per/100)

amnt_budget_hdd_ = budget - amnt_budget_ram_

total_cost_ram = (amnt_budget_ram_ * cost_ram_)_
total_cost_hdd = (amnt_budget_hdd_  * cost_hdd_)

print('you can afford', str(total_cost_hdd), 'gigs of hard-drive storage')
print('you can afford',str(total_cost_ram), 'gigs of RAM')