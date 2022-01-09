# ![alt text](http://AlgoExpert/Easy/files/img4.png)
def tournamentWinner(competitions, results):
    # Write your code here.
	scoreboard = {}
	
	for team, res in zip(competitions, results):
		if team[not res] not in scoreboard.keys():
			scoreboard.update({team[not res]:1})
		else:
			scoreboard.update({str(team[not res]):scoreboard[team[not res]]+1})
	
	winner=0
	team_name="India"
	for key,value in scoreboard.items():
		if value >= winner:
			winner=value
			team_name=key
	
    return team_name