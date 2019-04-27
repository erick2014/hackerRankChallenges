#!/usr/local/bin/python3

def getRankingsFromScores(scores,aliceScore):
    aliceRankingPosition = 0
    currentRanks = [1]
    greaterScore = 0
    greaterRankingPos = 0

    for i in range(1,len(scores)):
        currentScore = i
        previousScore = currentScore -1

        currentScoreValue = scores[currentScore]
        previousScoreValue = scores[previousScore]
        
        if(scores[currentScore] == scores[previousScore]):
            newScore= currentRanks[previousScore]

            if currentScoreValue > aliceScore:
                greaterScore = currentScoreValue
                greaterRankingPos = currentRanks[previousScore]

        else:
            newScore = (currentRanks[previousScore])+1
            
            if previousScoreValue > aliceScore:
                greaterScore = previousScoreValue
                greaterRankingPos = currentRanks[previousScore]

            if currentScoreValue > aliceScore:
                greaterScore = currentScoreValue
                greaterRankingPos = currentRanks[previousScore]+1

        currentRanks.append(newScore)

    if greaterScore == 0:
        aliceRankingPosition = 1
    
    if aliceScore < greaterScore:
        aliceRankingPosition = greaterRankingPos+1

    return aliceRankingPosition


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, aliceScores):
    aliceRankings = []
    
    for aliceScore in aliceScores:
        aliceRankingPosition = getRankingsFromScores(scores,aliceScore)
        aliceRankings.append(aliceRankingPosition)

    return aliceRankings


scoresCount = 0
scores = []
aliceGames = 0
aliceScores = []

# read line by line the config needed
scoresInFile = open("climbingTheBoard200000Input.txt","r")

with scoresInFile as sB:
    lineCounter = 1
    
    for line in sB:
        scoreLine=[]

        if(lineCounter==1):
            scoresCount = int(line)

        if(lineCounter==2):
            scoreLine =line.rstrip().split()
            scores = list(map(int,scoreLine))

        if(lineCounter==3):
            aliceGames = line.rstrip().split()
            aliceGames = int(aliceGames[0])

        if(lineCounter==4):
            scoreLine =line.rstrip().split()
            aliceScores = list(map(int,scoreLine))

        lineCounter+=1

scoresInFile.close()

# scores = [100,90,90,80,75,60]
# aliceScores = [50,65,77,90,102]

result = climbingLeaderboard(scores, aliceScores)
print(result)

# [100,100,50,40,40,30,20,10]
# [1, 1, 2, 3, 3, 4, 5]

# first find the index for the new added item
# if the new item was found and is in the position 0, set 1 as ranking
# if the previous value is equal to the new value, then grab from the ranking list in the previous position the ranking
# if the previous valus is different from the new score, then grab the previous ranking value and add one to it