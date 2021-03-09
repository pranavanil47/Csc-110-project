def calculate_distance(x1, y1, x2, y2):
    x_cordinates = (int(x1) - int(x2))
    y_cordinates = (int(y1) - int(y2))

    x_cordinates= x_cordinates ** 2
    y_cordinates= y_cordinates ** 2
    distance = (x_cordinates + y_cordinates) ** (1/2)
    distance = round(distance, 4)
    return distance

