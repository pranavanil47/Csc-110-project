from graphics import graphics
def main():
    gui = graphics(2000, 800, 'Lines')
    i = 50
    while i < 1000:
        if i % 100 == 0:
            gui.ellipse(i, i, 20, 20, 'khaki')
        else:gui.line(i, 0 , i, 1000, 'green', 10)
        i+= 25
    gui.primary.mainloop()
    
main()