#!/bin/python3

import sys
# d1 - m1 - y1 is the date when the book was returned
# d2 - m2 - y2 is the date to return the book
def libraryFine(d1, m1, y1, d2, m2, y2):
	# fine value to pay if the due date has expired
	fineDay = 15
	fineMonth = 500
	fineYear = 10000
	fineToPay = 0

	# the book has been delivery late in days
	if d1>d2 and m1<=m2 and y1<=y2: fineToPay = (d1-d2) * fineDay
	# the book has been delivery late in months
	elif m1>m2 and y1<=y2: fineToPay = (m1-m2)* fineMonth
	elif y1>y2: fineToPay =fineYear

	return fineToPay
		

if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)