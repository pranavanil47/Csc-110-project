from graphics import graphics
def main():
    gui = graphics(500, 500, 'graphics')
    offset = -700
    while True:
        gui.clear()
        i = 50
        while i < 550:
            gui.rectangle(0, i-50, offset+i, 50, 'blue')
            gui.triangle(0, i-50, 0, i, offset+i, i, 'green')
            i += 50
        offset += 5
        gui.update_frame(30)
main()
