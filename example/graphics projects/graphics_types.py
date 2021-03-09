from graphics import graphics

def types():
    gui = graphics(1920, 1080, 'Types')
    gui.rectangle(50, 10, 200, 100, 'black')
    gui.mouse_x
    gui.mouse_y
    gui.ellipse(150, 300, 200, 100, 'blue')
    gui.line(1500,150, 500, 500, 'red', 8 )
    gui.triangle(600, 600, 1000, 600, 800, 300, 'blue' )
    gui.primary.mainloop()

types()