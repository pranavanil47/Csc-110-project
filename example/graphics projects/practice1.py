from graphics import graphics

def triangle(gui,x,y,color):
    gui.triangle(x,y,x+100,y,x+50,y-100,color)

def color(gui):
    red,blue,green = 238,130,238
    color = gui.get_color_string(red,blue,green)
    return color

def main():
    gui = graphics(500,500,'Hi')
    purple = color(gui)
    while True:
        gui.clear()
        mouse_x = gui.mouse_x - 50
        mouse_y = gui.mouse_y + 45
        triangle(gui,mouse_x,mouse_y,purple)
        gui.update_frame(30)

main()
