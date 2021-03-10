import random

random_number = random.randint(0, 99)
if random_number < 20:
    print('small')
elif random_number >= 75:
    print('large')
else:
    print('medium')