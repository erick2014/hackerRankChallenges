def fruitsNearSamHouse(fruits,samHouseStarPoint, samHouseEndPoint):
    fruitsCounter = 0

    for fruit in fruits:
        if fruit >= samHouseStarPoint and fruit <= samHouseEndPoint:
            fruitsCounter+=1

    return fruitsCounter


def countApplesAndOranges(startingPointSam, endingPointSam, appleTreePoint, orangeTreePoint, apples, oranges):
   
    def getApplePosition(currentApplePos):
        return appleTreePoint + currentApplePos 

    def getOrangePosition(currentApplePos):
        return orangeTreePoint + currentApplePos 

    appleLandingPositions = list(map(getApplePosition,apples))
    orangeLandingPositions = list(map(getOrangePosition,oranges))

    applesNearSamHouse = fruitsNearSamHouse(appleLandingPositions,startingPointSam,endingPointSam)
    orangesNearSamHouse = fruitsNearSamHouse(orangeLandingPositions,startingPointSam,endingPointSam)

    print(applesNearSamHouse)
    print(orangesNearSamHouse)
    
'''
    demo input data to test
    7 11
    5 15
    3 2
    -2 2 1
    5 -6
'''

if __name__ == '__main__':
    samHousePoint = input().split()

    startingPointSam = int(samHousePoint[0])
    endingPointSam = int(samHousePoint[1])

    TreePoints = input().split()

    appleTreePoint = int(TreePoints[0])
    orangeTreePoint = int(TreePoints[1])

    fruitsQuantity = input().split()

    appleTreeFruitsQuantity = int(fruitsQuantity[0])
    orangeTreeFruitsQuantity = int(fruitsQuantity[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(startingPointSam, endingPointSam, appleTreePoint, orangeTreePoint, apples, oranges)