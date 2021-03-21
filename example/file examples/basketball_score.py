def save_points_file(players, points):
    file_name = input('Enter points file name: ')
    points_file = open(file_name, 'w')
    for i in range(len(players)):
        points_file.write(players[i]+ ' '+ str(points[i]))
        points_file.write('\n')
    points_file.close()

def get_command():
    user_input = input('Cmd: ')
    return user_input.split(' ')

def get_index(players, points, player):
    if player not in players:
        players.append(player)
        points.append(0)
    return players.index(player)

def show_scores(players, points):
    for i in range(len(players)):
        print(players[i] + ': ' +str(points[i]))

def load_points_file(players, points):
    file_name = input('Enter points file name: ')
    points_file = open(file_name, 'r')
    for line in points_file:
        line_split = line.split(' ')
        players.append( line_split[0] )
        points.append( int(line_split[1]) )

def main():
    players = []
    points = []
    load_points_file(players, points)
    while True:
        command = get_command()
        command_type = command[0]
        if command_type == 'ADD':
            index = get_index(players, points, command[1])
            points[index] += int(command[2])
        elif command_type == 'GET':
            index = get_index(players, points, command[1])
        elif command_type == 'SHOW':
            show_scores(players,points)
            print(command[1], 'has', points[index], 'points.')
        elif command_type == 'EXIT':
            return
        else:
            print('Huh?')

main()
