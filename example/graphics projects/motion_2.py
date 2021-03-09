from graphics import graphics

def motion():
    gui = graphics(700, 500, 'sup'  )
    cordx = 0
    cordy = 0
    while True:
        gui.clear()
        gui.rectangle(cordx, cordy, 50, 50, 'blue')

        if cordx > 750:
            cordx = -7
            cordy = -5
        cordx += 7
        cordy += 5
        gui.update_frame(30)
        #gui.primary.mainloop()

motion()