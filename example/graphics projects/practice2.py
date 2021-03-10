from graphics import graphics
import random

def draw_aquare(gui):
    x = 0
    y = 100

    gui.rectangle(x,y,100,100,'blue')
    gui.rectangle(x+100,y,100,100,'red')
    gui.rectangle(x+200,y,100,100,'green')


def main():
    gui = graphics(500, 500,'hello')
    draw_aquare(gui)
    gui.primary.mainloop()

main()