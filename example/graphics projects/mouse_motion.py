from graphics import graphics

def motion():
    gui = graphics(1000, 700, 'sup'  )
    while True:
        gui.clear()
        gui.rectangle(gui.mouse_x, gui.mouse_y, 50, 50, 'blue')
        gui.update_frame(30)
        #gui.primary.mainloop()

motion()