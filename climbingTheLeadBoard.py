#!/usr/local/bin/python3
from math import floor

def binarySearch (itemList, valueToFind) :
    start = 0
    stop = len(itemList) -1 
    middle = floor((start + stop) / 2)

    while (itemList[middle] != valueToFind and start < stop) :
         
        if valueToFind < itemList[middle] :
            start = middle + 1
        else:
            stop = middle - 1
    
        middle = floor((start + stop) / 2)

    #if the current middle item is what we're looking for return it's index, else return -1
    if itemList[middle] != valueToFind:
        return -1
    else:
        return middle

def getRankingsFromScores(scores):
    currentRanks = [1]
    
    for i in range(1,len(scores)):
        currentScore = i
        previousScore = currentScore -1
        
        if(scores[currentScore] == scores[previousScore]):
            newScore= currentRanks[previousScore]
        else:
            newScore = (currentRanks[previousScore])+1

        currentRanks.append(newScore)
    
    return currentRanks

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, aliceScores):
    currentRankings = getRankingsFromScores(scores)
    aliceRankings = []

    for aliceScore in aliceScores:
        newScores = scores.copy()
        # append the alice's score to the current scores
        newScores.append(aliceScore)
        # sort the scores in descending order
        newScores.sort()
        newScores = newScores[::-1]

        positionForAddedScore = binarySearch(newScores,aliceScore)
        positionBeforeForNewScore = positionForAddedScore-1
        newRanking = 0
        print('newScores ',newScores)
        print('aliceScore ',aliceScore)
        print('positionForAddedScore ',positionForAddedScore)

        if positionBeforeForNewScore <= 0 :
            aliceRankings.append(1)

        elif newScores[positionBeforeForNewScore] == newScores[positionForAddedScore] :
            newRanking = currentRankings[positionBeforeForNewScore]
            aliceRankings.append(newRanking) 

        elif newScores[positionBeforeForNewScore] != newScores[positionForAddedScore]:
            newRanking = currentRankings[positionBeforeForNewScore]+1
            aliceRankings.append(newRanking)

    return aliceRankings


scoresCount = 0
scores = []
aliceGames = 0
aliceScores = []

# read line by line the config needed
# scoresInFile = open("climbingTheBoard200000Input.txt","r")

# with scoresInFile as sB:
#     lineCounter = 1
    
#     for line in sB:
#         scoreLine=[]

#         if(lineCounter==1):
#             scoresCount = int(line)

#         if(lineCounter==2):
#             scoreLine =line.rstrip().split()
#             scores = list(map(int,scoreLine))

#         if(lineCounter==3):
#             aliceGames = line.rstrip().split()
#             aliceGames = int(aliceGames[0])

#         if(lineCounter==4):
#             scoreLine =line.rstrip().split()
#             aliceScores = list(map(int,scoreLine))

#         lineCounter+=1

# scoresInFile.close()

scores = [100,90,90,80,75,60]
aliceScores = [50,65,77,90,102]

result = climbingLeaderboard(scores, aliceScores)
print(result)

# [100,100,50,40,40,30,20,10]
# [1, 1, 2, 3, 3, 4, 5]

# first find the index for the new added item
# if the new item was found and is in the position 0, set 1 as ranking
# if the previous value is equal to the new value, then grab from the ranking list in the previous position the ranking
# if the previous valus is different from the new score, then grab the previous ranking value and add one to it