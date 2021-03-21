###
### Author: Pranav I Anilkumar  
### Class: CSc 110
### Description: A program that summarizes a log ile of a game (.txt) and summarizes
###              the game to give the winner, scores of each teams, and who scored 
###              first and last.
###

def split_list(game_file,points_list,team_list,players):
    '''
    This function splits the content in the text file into three lists; a list of
    all the points, teams and players in order of scoring.

    Parameters;
    game_file: This can be any text file with the specific format(team player points).
    point_list: This is a list of all points in the order of scoring.
    team_list:  This list is the order of scoring of two teams.
    players: This list is the scorers of the match im order. 
    '''
    points_file = open(game_file,'r')
    for line in points_file:
        k = line.split(' ')
        team_list.append(k[0])
        players.append(k[1])
        p = k[2]
        points = (p[:1])   ##Getting rid of '\n'
        points_list.append(int(points)) 

def teams(team_list):
    '''
    This functions specifies the two teams as different string and returns two 
    teams in order of the scoring.

    Parameters;
    team_list:  This list is the order of scoring of two teams.

    '''
    team1 = team_list[0]
    team2 =''
    i =1
    while i <len(team_list):   ## loopin until a different string to team1 is found
        if team_list[i]!= team1:
            team2+= team_list[i]
            i = len(team_list)
        else:
            i+=1
    return team1, team2


def summarizer(points_list,team_list,team1,team2):
    '''
    This function calculates the total points scored by both the teams and checks
    for the winner and returns the total score of each team and the winner.
    
    Parameters;
    point_lists: This is a list of all points in the order of scoring.
    team_list:  This list is the order of scoring of two teams.
    team1 = This is string obtained from the teams function.
    team2 = This is string obtained from the teams function.
    '''
    team1_total = 0
    team2_total = 0
    for i in range(len(team_list)):   ## looping to get total scores of each teams.
        if team_list[i] == team1:
            team1_total +=  points_list[i]
        else:
            team2_total+=points_list[i]
    
    if team1_total>team2_total:      ## Finding the winner.
        winner = team1
    else:
        winner = team2 
    return team1_total, team2_total, winner

def summarizer_print(players_list, team1, team1_points, team2, team2_points,winner):
    '''
    This function prints out the required output with the information about the 
    winner, each team scores and information on who scored first and last.

    Paramters;
    players_list: This list is the scorers of the match im order.
    team1 = This is string obtained from the teams function.
    team2 = This is string obtained from the teams function.
    team1_points = This is an integer obtained from the summarizer function.
    team2_points = This is an integer obtained from the summarizer function.
    winner = This is a string showing the winner of the game obtained from the
             summarizer function  

    '''
    print(winner, 'won!')
    print(team1, 'scored', team1_points, 'points.')
    print(team2, 'scored', team2_points, 'points.')
    print(players_list[0], 'scored first.')
    print(players_list[-1], 'scored last.' )


  
def main():
    game_file = input('enter gamelog file name:\n')
    team_list=[]
    points_list=[]
    players_list = []
    split_list(game_file,points_list,team_list,players_list)
    team1, team2 = teams(team_list)
    team1_points, team2_points,winner =summarizer(points_list,team_list,team1,team2)
    summarizer_print(players_list, team1, team1_points, team2, team2_points,winner)
    
main()

