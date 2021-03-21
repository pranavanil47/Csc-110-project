from graphics import graphics

def black_pin(gui, mouse_x, mouse_y):
    draw_pin(gui, mouse_x, mouse_y, 'black')

def main():
    gui = graphics(1000, 1000, 'run map')
    gui.set_right_click_action(black_pin)
    gui.image(0, 0, 1, 1, 'tenor.gif')
    path_file_name = input('Run file: ')
    path_file= open(path_file_name, 'r')
    lines = path_file.readlines()
    draw_path(gui, lines)

def draw_pin(gui, x, y, color):
    gui.triangle(x, y, x-10, y-30, x+10, y-30, color)
    gui.ellipse(x, y-35, 30, 30, color)
    gui.ellipse(x, y-35, 7, 7, 'white')

def draw_start(gui, x, y):
    draw_pin(gui, x, y, 'green')
    gui.text(x-24, y-75, 'start', 'black', 25)

def draw_finish(gui, x, y):
    draw_pin(gui, x, y, 'red')
    gui.text(x-27, y-75, 'finish', 'black', 25)

def draw_path(gui, path_file_lines):
    iteration = 0
    prev_x = -1
    prev_y = -1
    for line in path_file_lines:
        coordinates = line.split(',')
        x = int(coordinates[0])
        y = int(coordinates[1])
        if iteration == 0:
            draw_start(gui, x, y)
        elif iteration == len(path_file_lines)-1:
            draw_finish(gui, x, y)
        else:
            draw_pin(gui, x, y, 'blue')
        if prev_x != -1:
            gui.line(prev_x, prev_y, x, y, 'black', 5)
        prev_x = x
        prev_y = y
        gui.update_frame(1)
        iteration += 1

main()
