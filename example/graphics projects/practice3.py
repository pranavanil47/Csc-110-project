from graphics import graphics
def main():
    gui = graphics(400, 600, "Art")
    gui.line(0, 0, 400, 600, "black")
    gui.line(0, 600, 400, 0, "black")
    for i in range(0, 300, 50):
        gui.ellipse(i + 50, i + 100, 25, 25, "green")
        gui.triangle(50, 600, 350, 600, 200, 350, "blue")
        gui.triangle(100, 600, 300, 600, 200, 400, "purple")
    gui.primary.mainloop()
main()