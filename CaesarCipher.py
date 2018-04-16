def caesarCipher(s, k):
    # concatenate phrase encrypted
    phraseEncrypted = ''
    alphabet = 	 ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # get the alphabet size
    alphabetSize = len(alphabet)

    # split the list from the rotation num to the end of the list
    alphabetWithRotation = alphabet[k::]
    # split the list from the rotation number to the beginning of the list
    alphabetRotatedStart = alphabet[:k]
    # join the to lists
    alphabhetRotated = alphabetWithRotation+alphabetRotatedStart
    
    # loop each letter from the phrase
    for letter in s:
        currentLetter = letter
        # catch any exception if the item was not found
        try:
            # look for the letter in the normal alphabet
            letterFound = alphabet.index(currentLetter.lower(),0,alphabetSize)
            # get the encrypted letter
            letterEncrypted= alphabhetRotated[letterFound]
            # current letter is upper?
            if currentLetter.isupper() :
                # if is upper concatenate the latter as it is
                phraseEncrypted+=letterEncrypted.upper()
            else:
                phraseEncrypted+=letterEncrypted

        except ValueError:
            phraseEncrypted+=currentLetter
    
    return phraseEncrypted
		

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)