inventories = { 'ace': ['pliers', 'saw', 'shovel'],
                'home depot': ['pliers', 'lumber', 'shovel', 'drywall', 'foam'],
                'lowes': ['paint', 'tape', 'pliers'] }

def where_to_purchase(dict,item_list):
    for key,value in dict.items():
        for item in item_list:
            if item in value:
                a = True
            else:
                a = False
        if a == True:
            print(key)
        
where_to_purchase(inventories, ['shovel', 'pliers', 'drywall'])