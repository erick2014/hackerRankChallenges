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
    

if __name__ == '__main__':
    # samHousePoint = input().split()

    # startingPointSam = int(samHousePoint[0])
    startingPointSam = 7

    #endingPointSam = int(samHousePoint[1])
    endingPointSam = 11

    #TreePoints = input().split()

    # appleTreePoint = int(TreePoints[0])
    appleTreePoint = 5

    # orangeTreePoint = int(TreePoints[1])
    orangeTreePoint = 15

    #fruitsQuantity = input().split()

    #appleTreeFruitsQuantity = int(fruitsQuantity[0])
    appleTreeFruitsQuantity = 3

    #orangeTreeFruitsQuantity = int(fruitsQuantity[1])
    orangeTreeFruitsQuantity = 2

    # apples = list(map(int, input().rstrip().split()))
    apples = [-2,2,1]

    #oranges = list(map(int, input().rstrip().split()))
    oranges = [5,-6]

    countApplesAndOranges(startingPointSam, endingPointSam, appleTreePoint, orangeTreePoint, apples, oranges)