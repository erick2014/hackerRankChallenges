"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.

  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

  Sample Input
  array  = [3, 5, -4, 8, 11, 1, -1, 6]
  targetSum = 10

  Sample Output
  [-1, 11]
"""

def getTestCases():
    return {
        1: {
            "array": [3, 5, -4, 8, 11, 1, -1, 6],
            "targetSum": 10
        },
        2: {
            "array": [4, 6],
            "targetSum": 10
        },
        3: {
            "array": [4, 6, 1],
            "targetSum": 5
        },
        4: {
            "array": [4, 6, 1, -3],
            "targetSum": 3
        },
        5: {
            "array": [1, 2, 3, 4, 5, 6, 7, 8, 9],
            "targetSum": 17
        },
        6: {
            "array": [1, 2, 3, 4, 5, 6, 7, 8, 9, 15],
            "targetSum": 18
        },
        7:  {
            "array": [-7, -5, -3, -1, 0, 1, 3, 5, 7],
            "targetSum": -5
        }
        
    }

# This approach fails with this test case = [4, 6, 1, -3], targetSum = 3
def findTargetNumberSolutionOne(array,targetSum):
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

"""
    Complexity: 
        Time=O(N) --> because we just go through the array only once
        Space=O(N) --> because we have a hash map
    Solution works as expected
"""
    #[3, 5, -4, 8, 11, 1, -1, 6], targetSum = 10
def findTargetNumberSolutionTwo(array,targetSum):
    remindersDict = {}
    firstNumber = array[0]
    reminder = targetSum - firstNumber
    remindersDict[firstNumber] = 1

    for i in range(1,len(array)):
        currentNumber = array[i]
        reminder = targetSum - (currentNumber)

        if reminder in remindersDict :
            return [currentNumber,reminder]
        else:
            remindersDict[currentNumber] = 1
    
    return []

"""
    # [3,5,-4,8,11,1,-1,6] -> sorted= [-4, left(-1), 1, 3, 5, 6, 8, right(11)]
    Complexity:
        Time=O(N log(n))
        Space=O(1)
"""
def findTargetNumberSolutionThree(array,targetSum):
    arraySorted = sorted(array)
    leftPointer = 0
    rightPointer = len(arraySorted) - 1
    
    for i in array:
        leftNumber = arraySorted[leftPointer]
        rightNumber = arraySorted[rightPointer]
        reminder =  leftNumber + rightNumber
        
        if reminder == targetSum:
            return [leftNumber,rightNumber]

        if reminder > targetSum:
            rightPointer-=1
        elif reminder < targetSum:
            leftPointer+=1

    return []


tests = getTestCases()
for i in tests:
    testArray = tests[i]["array"]
    testTargetSum = tests[i]["targetSum"]
    message = "array:{}, targetSum: {}".format(testArray,testTargetSum)
    print(message)
    result = findTargetNumberSolutionTwo(testArray,testTargetSum)
    print("my output= {}".format(result))
    print("")

# print(findTargetNumberSolutionThree([3,5,-4,8,11,1,-1,6],13))