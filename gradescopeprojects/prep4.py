###
###Author : Pranav I Anilkumar
### Class : CSc 110
### Description : A program that prints out 3 conversions of feel; inches, meters and rods. meters rounded to 3 decimal  
###               places and rods rounded to one decimal places 
###

feet= int(input('Number of feet:\n'))
print('')

inches = (feet * 12)
meters = round(feet *  0.3048, 3 )
rods =  round(feet/16.5,1)

print('Inches:', inches)
print('Meter:', meters)
print('Rods:', rods) 