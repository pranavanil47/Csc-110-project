from graphics  import graphics
import random
def main():
    gui = graphics(1000, 700, 'sup')
    color = 'blue'
    frame_counter = 0
    while True:
        gui.clear()
        gui.rectangle(gui.mouse_x -100, gui.mouse_y -100, \
            200, 200, color)
        frame_counter += 1
        if frame_counter == 30:
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            frame_counter = 0
            color = gui.get_color_string(red, green, blue)
        gui.update_frame(30)

main()