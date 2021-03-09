from graphics import graphics
import random

def mountain(gui):    
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    color = gui.get_color_string(red, green, blue)
    while True:
        gui.clear()
        gui.rectangle(gui.mouse_x,gui.mouse_y,100,50, color)
        gui.update_frame(30)


def main():
    gui = graphics(800,800, 'check')
    mountain(gui)
    gui.primary.mainloop()

main()  