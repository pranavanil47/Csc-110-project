###
### Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that determines whether or not the specified CPU is
###               within one of four categories: high-performance, medium-performance,    
###               low-performance, and in need of an upgrade.
###


import os 
clock_speed = float(input('Enter CPU gigahertz:\n'))
cores = int(input('Enter CPU core count:\n'))
print(' ')

if cores < 2 or clock_speed < 2.0:
    print('That CPU could use an upgrade.')
    
if 2 <= cores <6:
    if 2.0<= clock_speed <2.5:
        print('That is a low-performance CPU.')
    if 2.5<= clock_speed <3.2:
        print('That is a low-performance CPU.')
    if clock_speed >= 3.2:
        print('That is a low-performance CPU.')
    
if 6 <= cores < 8:
    if 2.0<= clock_speed <2.5:
        print('That is a low-performance CPU.')
    if 2.5<= clock_speed <3.2:
        print('That is a medium-performance CPU.')
    if clock_speed >= 3.2:
        print('That is a medium-performance CPU.')

if 8<= cores < 20:
    if 2.0<= clock_speed <2.5:
        print('That is a low-performance CPU.')
    if 2.5<= clock_speed <3.2:
        print('That is a medium-performance CPU.')
    if clock_speed >= 3.2:
        print('That is a high-performance CPU.')

if cores >= 20:
    print('That is a high-performance CPU.')

os._exit(0)
             