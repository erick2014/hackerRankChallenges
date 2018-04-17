'''
	test case 1 input:
	10
	159357lcfd
	98

	test case 1 output:
	159357fwzx

	test case 2 input:
	11
	middle-Outz
	2

	test case 2 output
	okffng-Qwvb
'''

def caesarCipher(s, k):
	# concatenate encrypted characteres
	phraseEncrypted = ''
	alphabet = 	 'abcdefghijklmnopqrstuvwxyz'
	sizeToRotate = 0 

	if k >= len(alphabet) : sizeToRotate = k % len(alphabet)
	else: sizeToRotate = k
	
	# join the alphabeth rotating the positions we received as param
	alphabetRotated = alphabet[sizeToRotate::]+alphabet[:sizeToRotate]
	
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