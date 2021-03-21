def get_file():
    file_name = input('Enter the game file: ')
    points_file = open(file_name, 'w')
    points_file.write('team player points\n')
    points_file.close()
    return file_name

def add_score(game_file, team,player, points):
    points_file = open(game_file, 'w')
    points_file.a


def split_list(game_file):
    pass
def main():
    get_file()
    pass

main()