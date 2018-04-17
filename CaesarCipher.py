def caesarCipher(s, k):
	# concatenate encrypted characteres
	phraseEncrypted = ''
	alphabet = 	 'abcdefghijklmnopqrstuvwxyz'
	# get the alphabet size
	alphabetSize = len(alphabet)
	# join the alphabeth rotating the positions we received as param
	alphabetRotated = alphabet[k::]+alphabet[:k]
	
	# loop each letter from the phrase
	for letter in s:
		# look for the letter in the normal alphabet
		letterFound = alphabet.find(letter.lower())
		
		if(letterFound!=-1) :	
			# get the encrypted letter
			letterEncrypted= alphabetRotated[letterFound]
			# current letter is upper?
			if letter.isupper() :
				# if is upper concatenate the latter as it is
				phraseEncrypted+=letterEncrypted.upper()
			else:
				phraseEncrypted+=letterEncrypted
		else:
			phraseEncrypted+=letter
	
	return phraseEncrypted
		

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)