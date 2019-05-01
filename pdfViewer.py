def designerPdfViewer(heightList, word):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    wordLettersCounter = 0
    letterWithGreaterHeight = 0

    for letter in word:
        wordLettersCounter+=1

        letterIndex = letters.index(letter)
        letterHeight = int(heightList[letterIndex])

        if letterHeight > letterWithGreaterHeight:
            letterWithGreaterHeight = letterHeight

    sizeOfHighlightedWord = letterWithGreaterHeight * wordLettersCounter

    return sizeOfHighlightedWord


heights = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7"
heightList = heights.split(" ")

result = designerPdfViewer(heightList,"zaba")
print(result)