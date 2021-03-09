


from graphics import graphics
import random 

def square(gui, x, y):
    '''
    This function prints a square with specific dimensions.
    x: can be any integer 
    y: can be any integer
    '''    
    gui.rectangle(x, y, 100, 100, 'red')
    

def circle(gui, x, y):
    '''
    This function prints a circle with specific dimensions.
    x: can be any integer 
    y: can be any integer
    '''
    gui.ellipse(x + 50, y, 100, 100, 'blue' )
    

def triangle(gui, x, y):
    '''
    This function prints a triangle with specific dimensions.
    x: can be any integer 
    y: can be any integer
    '''
    gui.triangle(x , y, x + 100, y, x + 50, y - 100, 'green' ) #Here i put all cordinates wrt to x and y
                                                      #to get a triangle with specific measurements .

def motion(gui):
    '''
    This function contains all the print statements and 
    the motion statement
    gui is graphical user interface
    '''
    x_cordinate = 100
    y_cordinate_1 = 100 #Had to create different y index
    y_cordinate_2 = 100 #variable to give randomness to
    y_cordinate_3 = 100 # y-cordinate
    
    while True:
        gui.clear() 
        square(gui, x_cordinate, y_cordinate_1 )
        circle(gui, x_cordinate, y_cordinate_2)
        triangle(gui, x_cordinate, y_cordinate_3)

        if x_cordinate > 700:                       ## Creating a loop to create a wrap
            x_cordinate = -100                      ## -around and reset y cordinate
            y_cordinate_1 = random.randint(10, 500) 
            y_cordinate_2 = random.randint(10, 500) ## for every wrap-around y-cordinate is random
            y_cordinate_3 = random.randint(10, 500)
        x_cordinate += 10
        gui.update_frame(30)
    
def main():
    '''
    This is the main function has the canvas in which  
    the program runs and the calls the motion function
    ''' 
    gui = graphics(600, 600, 'Three')
    motion(gui)
   

main()