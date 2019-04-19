#!/usr/local/bin/python3

def removeDuplicatedScores(scores):
    leadBoardScores = scores.copy()
    uniqueScores = []
    # remove duplicated items
    for leadScore in leadBoardScores:
       if not(leadScore in uniqueScores):
           uniqueScores.append(leadScore)

    return uniqueScores

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, aliceScores):
    leadBoardScores = removeDuplicatedScores(scores)
    aliceRanksInLeadBoard = []

    for aliceScore in aliceScores:
        newLeadBoardScores = leadBoardScores.copy()
        # append the alice's score to the current scores
        newLeadBoardScores.append(aliceScore)
        # sort the scores in descending order
        newLeadBoardScores.sort()
        newLeadBoardScores = newLeadBoardScores[::-1]

        alicePositionInLeadBoard = newLeadBoardScores.index(aliceScore)+1
        aliceRanksInLeadBoard.append(alicePositionInLeadBoard)

    return aliceRanksInLeadBoard

scores_count = int(input())
scores = list(map(int, input().rstrip().split()))
aliceGames = int(input())
aliceGames = 4
aliceScores = list(map(int, input().rstrip().split()))
result = climbingLeaderboard(scores, aliceScores)
print(result)