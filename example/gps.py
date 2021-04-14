import webbrowser
def get_location_info():
    location_info = {}
    location_file = open('locations.csv','r')

    for line in location_file:
        values = line.split(',')
        location_info[values[0]] = (values[1],values[2])
    return location_info

def main():
    location = get_location_info()
    url_base = 'https://www.google.com/maps/search/?api=1&query='
    city = input('Enter city')

    if city in location:
        url = url_base + location[city][0]+', '+location[city][1]
        webbrowser.open(url)
    else:
        print('lol')
main()