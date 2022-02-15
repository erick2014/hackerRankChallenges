def getTestCases():
    return {
        1: {
            "array": [-2, -1]
        },
        2: {
            "array": [-5, -4, -3, -2, -1]
        },
        3:{
            "array": [-50,-13,-2,-1,0,0,1,1,2,3,19,20]
        },
        4:{
            "array": [1, 2, 3, 5, 6, 8, 9]
        },
        5:{
            "array":[-10, -5, 0, 5, 10]
        },
    }
# Time O(n), space O(n)
def sortedSquaredArrayTwo(array):
    leftPointer = 0
    rightPointer = len(array) - 1
    # create an array filled with 0
    squaredArray = [0 for _ in array]
    
    for index in range(len(array)-1,-1,-1):
        leftNumber = abs(array[leftPointer])
        rightNumber = abs(array[rightPointer])
        
        if leftNumber > rightNumber:
            squaredArray[index] = leftNumber * leftNumber
            leftPointer+=1
        else:
            squaredArray[index] = rightNumber * rightNumber
            rightPointer-=1
        
    return squaredArray

# Time O(n), space O(n)
def sortedSquaredArray(array):
    leftPointer = 0
    rightPointer = len(array) - 1
    squaredArray = []
    counter = 0

    while len(squaredArray)< len(array) :
        leftNumber = abs(array[leftPointer])
        rightNumber = abs(array[rightPointer])
        counter +=1
        if leftNumber > rightNumber:
            squaredArray.insert(0,leftNumber*leftNumber)
            leftPointer +=1
        elif rightNumber > leftNumber:
            squaredArray.insert(0,rightNumber*rightNumber)
            rightPointer-=1
        elif leftNumber == rightNumber:
            if leftPointer ==rightPointer:
                squaredArray.insert(0,leftNumber *leftNumber)
            else:
                squaredArray.insert(0,leftNumber *leftNumber)
                squaredArray.insert(0,rightNumber *rightNumber)
            leftPointer+=1
            rightPointer-=1
    return squaredArray

tests = getTestCases()
for i in tests:
    testArray = tests[i]["array"]
    message = "array:{}".format(testArray)
    print(message)
    result = sortedSquaredArrayTwo(testArray)
    print("squared asc= {}".format(result))
    print("") 
 