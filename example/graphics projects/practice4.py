from graphics import graphics
def main():
    pos = [250, 50, 125, 250, 375, 250, 250, 50, 125, 250, 375, 250]
    screen = graphics(500, 300, 'Problem 4')
    while True:
        screen.clear()
        for i in range(0, len(pos), 4):
            screen.line(pos[i], pos[i+1], pos[i+2], pos[i+3])
        screen.update_frame(60)

main()