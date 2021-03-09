from graphics import graphics

def main():
    gui = graphics(700, 451, 'alternate lines')

    i = -150 
    while i < 700:
        if i % 100 == 0:
            gui.line(i , 0, i+200, 450, 'red', 20)
        else:
            gui.line(i , 0, i+200, 450, 'blue', 20)
        
        i += 50
    gui.primary.mainloop()
        
main()

