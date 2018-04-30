#!/bin/python3

import sys

def hackerrankInString(s):
	'''
		wordToMatch = {
		'h':1,'a':2,'c':1,'k':2,'e':1,'r':2,'n':1,
	}
	wordMatches ={
		'h':0,'a':0,'c':0,'k':0,'e':0,'r':0,'n':1,
	}
	queryStr = s.lower()
	for letter in queryStr:
		if letter in wordToMatch : 
			if int(wordMatches[letter]) < int(wordToMatch[letter]) :
				wordMatches[letter]= wordMatches[letter] + 1

	if wordToMatch == wordMatches: return "YES"
	else: return "NO"
	'''
	
	wordToMatch = 'hackerrank'
	wordMatches = ''

	queryStr = s.lower()
	for letter in queryStr:
		letterFound = wordToMatch.find(letter)
		# concatenate the letters that match
		if letterFound!=-1 : wordMatches+=letter

	
	return "YES"

def readInputFromTextFile():
	with open("HackerRankInAStringInput.txt") as f:
		content = f.readlines()
		for l in content:
			line = l.strip()
			result = hackerrankInString()
			print(result)

if __name__ == "__main__":
	readInputFromTextFile()
	# q = int(input().strip())
	# for a0 in range(q):
	# 	s = input().strip()
	# 	result = hackerrankInString(s)
	# 	print(result)
