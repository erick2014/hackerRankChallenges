"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4], and so do the numbers [2, 4]. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.
  
"""

def getTestCases():
    return {
        1: {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [1, 6, -1, 10]
        },
        2: {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [5, 1, 22, 25, 6, -1, 8, 10]
        },
        3: {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [5, 1, 22, 6, -1, 8, 10]
        },
        4: {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [22, 25, 6]
        },
        5: {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [1, 6, 10]
        },
        6: {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [5, 1, 22, 10]
        },
        7:  {
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence":[5, -1, 8, 10]
        },
        8:{
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 12]
        },
        9:{
            "array": [5, 1, 22, 25, 6, -1, 8, 10],
            "sequence": [1, 6, -1, -2]
        }
    }


def isValidSubsequence(array, sequence):
    validSequenceNumberCounter = 0
    for number in array:
        if validSequenceNumberCounter < len(sequence):
            isNumberInSequence = sequence[validSequenceNumberCounter]
            if number == isNumberInSequence:
                if validSequenceNumberCounter < len(sequence):
                    validSequenceNumberCounter+=1
    
    if validSequenceNumberCounter == len(sequence):
        return True
    else:
        return False
            

tests = getTestCases()

for i in tests:
    testArray = tests[i]["array"]
    testSequence = tests[i]["sequence"]
    message = "array:{}, sequence: {}".format(testArray,testSequence)
    print(message)
    result = isValidSubsequence(testArray,testSequence)
    print("my output= {}".format(result))
    print("")
