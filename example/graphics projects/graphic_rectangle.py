from graphics import graphics

def three_squares():
    gui = graphics(700,300, 'Three squares ')
    gui.rectangle(25, 50, 200, 200, 'black')
    gui.rectangle(250, 50, 200, 200, 'purple')
    gui.rectangle(475, 50, 200, 200, 'orange')
    gui.primary.mainloop()

three_squares()