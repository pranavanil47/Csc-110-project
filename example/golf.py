## for using boolean which is recomended check golfboolean.py 

import os

par = input('golf hole par:\n')

if par.isnumeric() == False:
    print('inavalid par')
    os._exit(0)

par = int(par)

if par < 1:
    print('Enter realistic par.')
    os._exit(0)
if par > 6:
    print('Enter realistic par.')
    os._exit(0)

swing = input('Enter swing')

if swing.isnumeric() == False:
    print('inavalid par')
    os._exit(0)

swing = int(swing)

if swing >= 7:
    print('u need a golf lesson\n')

if swing == par:
    print('ya on par')

if swing <= (par-1):
    print('oh ok')

else:
    print('ok u broke code')

os._exit(0)