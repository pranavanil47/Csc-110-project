from graphics import graphics

def main():
    gui = graphics(700, 300, 'Lines')
    i = 10
    while i < 700:
        gui.rectangle(i, 50, 20, 200, 'blue')
        gui.rectangle(200, i, 200, 20, 'blue')
        i += 70
    gui.primary.mainloop()

main()