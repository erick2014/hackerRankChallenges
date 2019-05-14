def bigSorting(unsorted):
    sorted = True
    sortedList = unsorted.copy()
    unsortedLength = len(unsorted)

    while sorted:
        sorted = False
        for number in range(len(unsorted)):
            nextNumber = number + 1
            if nextNumber == unsortedLength:
                break

            if unsorted[number] > unsorted[nextNumber]:
                currentNumberValue = unsorted[number]
                unsorted[number] = unsorted[nextNumber]
                unsorted[nextNumber] = currentNumberValue
                sorted = True

        if not sorted:
            break

    return unsorted

n = int(input())
unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(int(unsorted_item))

sortedList = bigSorting(unsorted)
sortedResult = []

for sortedNum in range(len(sortedList)):
    currentNum = sortedList[sortedNum]
    sortedResult.append(str(currentNum))
    print(currentNum)
