"""
   In this algorithm we find the team, that has more points, based on this criteria:
   [homeTeam, awayTeam], if we have 0 in results array it means awayTeam won 3 points, 
   but if we have 1 in results array, it means homeTeam won 3 points
   Complexity Time = O(N)
   Space = O(K +1 ) = O(k), this is because we need to store all the keys in a hashmap 
"""

def tournamentWinner(competitions, results):
    pointsByTeam = { }
    greaterTeamScore = 0
    greaterTeamName = ""
    for index in range(0,len(results)):
        winnerTeamResult = results[index]
        winnerTeamIndex = ""
        if(winnerTeamResult < 1):
            winnerTeamIndex = 1
        else:
            winnerTeamIndex = 0

        winnerTeamName = competitions[index][winnerTeamIndex]

        if winnerTeamName in pointsByTeam:
            pointsByTeam[winnerTeamName] +=3
        else:
            pointsByTeam[winnerTeamName] =3

        if(pointsByTeam[winnerTeamName]) > greaterTeamScore:
            greaterTeamName = winnerTeamName
            greaterTeamScore = pointsByTeam[winnerTeamName]
 
    return greaterTeamName

competitions= [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"],
    ["SQL", "C#"],
    ["HTML", "SQL"],
    ["SQL", "Python"],
    ["SQL", "Java"]
  ]
results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

print(tournamentWinner(competitions,results))