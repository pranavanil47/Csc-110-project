from graphics import graphics
def get_stock_data():
    f = open('stocks.csv', 'r')
    data = []
    for line in f:
        row = []
        sp = line.split(',')
        row.append(sp[0])
        row.append(sp[1])
        for element in sp[2:]:
            row.append(int(element))
        data.append(row)
    return data

def main():
    stock_data = get_stock_data()
    gui = graphics(600, 300, 'stocks')
    i = 0
    while i < len(stock_data):
        print(stock_data[i])
        color = stock_data[i][0]
        gui.text(5, 5+30*i, stock_data[i][1], color, 25)
        j= 0
        prev_x = -1
        prev_y = -1
        while j < len(stock_data[i])-2:
            x = 10 + (j*50)
            y = -(stock_data[i][j+2]-300)
            if prev_x >= 0:
                gui.line(prev_x, prev_y, x, y, color, 2)
            gui.ellipse(x, y, 10, 10, color)
            prev_x = x
            prev_y = y
            j += 1
        i += 1

main()

