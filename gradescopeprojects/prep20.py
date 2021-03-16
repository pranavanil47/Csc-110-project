def most_common_vehicle(file):
    car_file  = open(file, 'r')
    line = car_file.readline()
    supra = int(line)
    line = car_file.readline()
    mustang = int(line)
    line = car_file.readline()
    stingray = int(line)

    if (supra == mustang) or (supra == stingray) or mustang == stingray:
        print('There\'s a tie!')
    
    else:
        if max(stingray,mustang,supra) == stingray:
            print('Chevy most common')
        elif max(stingray,mustang,supra) == supra:
            print('Toyota most common')
        elif max(stingray,mustang,supra) == mustang:
            print('Ford most common')


