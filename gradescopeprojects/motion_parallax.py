###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: An animated program which shows a landscape with mountains
###              and trees which allows the user to control the perspective of the
###               mountains, ground, grass, tree and the sun or moon.Also a flock 
###               of birds fly around, there is a day night transition and snowfall!!!

from graphics import graphics
import random

def ground(gui,x,y):
    '''
    This function is used to print out the grass and
    the ground.
    parameters;
    x: can be any float
    y: can be any float
    the parameters sets the cordinates wrt a point
    '''
    gui.rectangle(3*x-100, 3*y+500, 700, 500, 'spring green')
    x_cordinate = -100
    while x_cordinate < 900:
        gui.line( x +x+ x_cordinate, 3*y + 600, x + x + x_cordinate,\
             3*y+ 475,'spring green', 2 )
        x_cordinate+= 10

def mountains(gui,x,y,color1,color2,color3):
    '''
    This fuction is used to print out three mountains with
    random numbers.
    parameters;
    x: can be any float
    y: can be any float
    color1: should be a one of specific color strings from graphics module.
    color2: should be a one of specific color strings from graphics module.
    color3: should be a one of specific color strings from graphics module.
    '''   
    gui.triangle(x+200, y+550, x+400, y+550, \
        x+300, y+200, color1 )
    gui.triangle(x-100, y+550, x+300, y+550,\
         x+150, y+300, color2 )
    gui.triangle(x+200, y+550, x+750, y+600,\
         x+500, y+300, color3)

def random_color(gui):
    '''
    This function is used to generate a random color string
    from the graphics module. 
    '''
    red = random.randint(0,255)
    green = random.randint(0,255) #gives out a random number between
    blue = random.randint(0,255)  # 0 and 255
    color = gui.get_color_string(red, green, blue)
    return color

def tree(gui,x,y):
    '''
    This function prints out the tree.
    parameters;
    x: can be any float
    y: can be any float
    '''
    gui.rectangle(x+500, y+500, 25, 75, 'brown')
    gui.ellipse(x+512, y+475, 65, 90, 'green')
    
def sun_moon(gui,x,y,colour):
    '''
    This function is used to print out either 
    the sun or the moon.
    x: can be any float
    y: can be any float
    color: should be a one of specific color strings from graphics module.
    ''' 
    gui.ellipse(x+450,y+100, 100, 100, colour)        

def paralax_movement(gui,color1,color2,color3):
    '''
    This function contains the functions needed to 
    call the paralax movements for mountains,ground
    and tree.
    parameters;
    color1: should be a one of specific color strings from graphics module.
    color2: should be a one of specific color strings from graphics module.
    color3: should be a one of specific color strings from graphics module.
    '''     
    x_mouse = gui.mouse_x/25 
    y_mouse = gui.mouse_y/25         
    mountains(gui,x_mouse,y_mouse,color1,color2,color3)    
    ground(gui,x_mouse,y_mouse)
    tree(gui,x_mouse,y_mouse)

def snow(gui,y):    
    ''' 
    This function helps to print the snow background.
    parameters;
    y: can be any integer
    '''
    gui.ellipse( 10, y+10, 7, 7, 'white')
    gui.ellipse(20, y+50, 7, 7, 'white')
    gui.ellipse(210,  y, 7, 7, 'white')
    gui.ellipse(430, y+100, 7, 7, 'white')
    gui.ellipse(305, y+150, 7, 7, 'white')
    gui.ellipse(250, y+200, 7, 7, 'white')
    gui.ellipse(470, y+250, 7, 7, 'white')
    gui.ellipse(50, y+300, 7, 7, 'white')
    gui.ellipse(450, y+350, 7, 7, 'white')
    gui.ellipse(30, y+400, 7, 7, 'white')
    gui.ellipse(550, y+400, 7, 7, 'white')
    gui.ellipse(600, y+100, 7, 7, 'white')
    gui.ellipse(600, y+150, 7, 7, 'white')
    gui.ellipse(500, y+100, 7, 7, 'white')

def birds_line(gui,x, y):
    '''
    This function is used to draw the birds.
    parameters;
    x: can be any float
    y: can be any float
    '''
    gui.line(x, y ,x+10, y+10, 'black', 2)
    gui.line(x+10, y+10, x+20 , y, 'black',2)

def birds(gui,i):
    '''
    This function contains the fuction used to 
    print multiple birds on the canvas.
    parameters;
    i: can be any integer
    '''
    x=0
    y=200
    while y<231:
        birds_line(gui,i +x ,y)
        y+=10
        x+=30
        

def main():
    '''
    This is  the main function where the canvas is  
    created, the background day night animation is
    created, while loop for all paralax movements,
    and bird movement animation.
    '''

    gui = graphics(600, 600, 'Motion paralax')
    color1 = random_color(gui)
    color2 = random_color(gui)
    color3 = random_color(gui)
    sun = 0                         #for the day night animation
    bird_x=10                          #for the bird animation
    snow_y = 0
    while True:
        x1_mouse = gui.mouse_x/50
        y1_mouse = gui.mouse_y/50
        gui.clear()
        if 0<= sun <=50:
            gui.rectangle(-10,-10,700,700, 'sky blue')
            sun_moon(gui,x1_mouse,y1_mouse,'yellow2') # Day night transition animation.
        elif 50 < sun <=100:
            gui.rectangle(-10,-10,700,700, 'gray25')
            sun_moon(gui,x1_mouse,y1_mouse, 'snow')
        elif sun>= 100:
            sun = 0
        sun+=1
        snow(gui,snow_y)
        if snow_y > 800:
            snow_y = -100
        snow_y+=5
        paralax_movement(gui,color1,color2,color3)
        birds(gui,bird_x)
        if bird_x > 700:
            bird_x = -100
        bird_x+= 8
        gui.update_frame(30)
    
        
        
main()
