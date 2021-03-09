from graphics import graphics

def motion1():
    gui = graphics(700, 500, 'sup'  )
    cord = 0
    while True:
        gui.clear()
        gui.rectangle(cord, 125, 50, 50, 'blue')

        if cord > 750:
            cord = -50
        cord += 10
        gui.update_frame(30)
        #gui.primary.mainloop()

motion1()