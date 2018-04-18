#!/bin/python3

import sys


def hackerrankInString(s):
	wordToMatch ='hackerrank'
	letterMatches = 0
  # Complete this function
	for letter in wordToMatch:
		if s.find(letter)!=-1 : letterMatches+=1
	
	if letterMatches == len(wordToMatch): return "YES"
	else: return "NO"


if __name__ == "__main__":
	q = int(input().strip())
	for a0 in range(q):
		s = input().strip()
		result = hackerrankInString(s)
		print(result)
