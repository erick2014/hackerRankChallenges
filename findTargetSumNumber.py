def getTestCases():
    return {
        1: {
            "array": [3, 5, -4, 8, 11, 1, -1, 6],
            "targetSum": 10,
            "expectedOutput" : [11,-1]
        },
        2: {
            "array": [4, 6],
            "targetSum": 10,
            "expectedOutput" : [4,6]
        },
        3: {
            "array": [4, 6, 1],
            "targetSum": 5,
            "expectedOutput" : [4,1]
        },
        4: {
            "array": [4, 6, 1, -3],
            "targetSum": 3
        },
        5: {
            "array": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "targetSum": 17,
            "expectedOutput": [8,9]
        },
        6: {
            "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 15],
            "targetSum": 18,
            "expectedOutput": []
        },
        7:  {
            "array": [-7, -5, -3, -1, 0, 1, 3, 5, 7],
            "targetSum": -5
        }
        
    }

# This approach fails with this test case = [4, 6, 1, -3], targetSum = 3
def findTargetNumberFirstApproach(array,targetSum):
    maxNumber = array[0]
    maxAcum = targetSum - maxNumber
    for i in range(1,len(array)):
        reminder = 0
        currentNumber = array[i]
        
        if (currentNumber+maxNumber) == targetSum:
            return [currentNumber,maxNumber]

        if(currentNumber > targetSum):
            reminder = currentNumber - targetSum
        else:
            reminder = targetSum - currentNumber

        if reminder < maxAcum :
            maxNumber = currentNumber
            maxAcum = reminder

    return []

# Solution works as expected
def findTargetNumber(array,targetSum):
    remindersDict = {}
    firstNumber = array[0]
    reminder = targetSum - firstNumber
    remindersDict[firstNumber] = targetSum - firstNumber

    for i in range(1,len(array)):
        currentNumber = array[i]
        reminder = targetSum - (currentNumber)

        if reminder in remindersDict :
            print(remindersDict)
            return [currentNumber,reminder]
        else:
            remindersDict[currentNumber] = reminder
    
    return []


tests = getTestCases()
for i in tests:
    testArray = tests[i]["array"]
    testTargetSum = tests[i]["targetSum"]
    mesage = "array:{}, targetSum: {}"
    result = findTargetNumber(testArray,testTargetSum)
    print("my output= {}".format(result))
    print("")

print(findTargetNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 15],18))

