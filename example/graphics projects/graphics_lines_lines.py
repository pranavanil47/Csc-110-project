from graphics import graphics

def main():
    gui = graphics(700, 500, 'alternate lines')

    i = 50 
    while i < 700:
        if i % 100 == 0:
            gui.line(i , 0, i, 450, 'red', 49)
        else:
            gui.line(i , 0, i, 450, 'blue', 49)
        
        i += 50
    gui.primary.mainloop()
        
main()

