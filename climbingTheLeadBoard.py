#!/usr/local/bin/python3

def getRankingsFromScores(scores):
    currentRanks = [1]

    for i in range(1,len(scores)):
        currentScore = i
        previousScore = currentScore -1

        currentScoreValue = scores[currentScore]
        previousScoreValue = scores[previousScore]
        
        if(scores[currentScore] == scores[previousScore]):
            newScore= currentRanks[previousScore]

        else:
            newScore = (currentRanks[previousScore])+1

        currentRanks.append(newScore)

    return currentRanks


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, aliceScores):
    aliceRankings = []
    continueLooping = True
    lowerScoreRankingPos = len(scores)-1
    currentRankingPositions = getRankingsFromScores(scores)

    for aliceScoreIndex in range(len(aliceScores)):
        aliceScore = aliceScores[aliceScoreIndex]
        continueLooping = True
        
        while continueLooping:
        
            if lowerScoreRankingPos == 0 and aliceScore < scores[lowerScoreRankingPos]:
                aliceRankings.append(currentRankingPositions[lowerScoreRankingPos+1])

            elif lowerScoreRankingPos == 0:
                continueLooping = False
                aliceRankings.append(1)
                break
           
            if aliceScore > scores[lowerScoreRankingPos]:  
                lowerScoreRankingPos = lowerScoreRankingPos -1

            elif aliceScore == scores[lowerScoreRankingPos]:
                aliceRankings.append(currentRankingPositions[lowerScoreRankingPos])
                lowerScoreRankingPos = lowerScoreRankingPos -1
                continueLooping = False

            else:
                if lowerScoreRankingPos > 0:
                    aliceRankings.append(currentRankingPositions[lowerScoreRankingPos]+1)
                
                continueLooping = False

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

# scores = [100,100,50,40,40,20,10]
# aliceScores = [5,25,50,120]

result = climbingLeaderboard(scores, aliceScores)
##print(result)

# [100,100,50,40,40,30,20,10]
# [1, 1, 2, 3, 3, 4, 5]

# first find the index for the new added item
# if the new item was found and is in the position 0, set 1 as ranking
# if the previous value is equal to the new value, then grab from the ranking list in the previous position the ranking
# if the previous valus is different from the new score, then grab the previous ranking value and add one to it