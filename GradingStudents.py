'''to calculate the greater number we do: m - r(reminder) + n
to calculate the smaller number we do: n - r(reminder)

n = 17 	m = 4 	17 / 4 = 4 	Reminder 1 	smaller = 16	greater = 20

n = 73 	m = 5		73 / 5 = 14 Reminder 3  smaller = 70	greater = 75

n = 67	m = 5		67 / 5 = 13 Reminder 2	smaller = 65	greater = 70

n = 38	m = 5		38 / 5 = 7	Reminder 3	smaller = 35	greater = 40

n = 33	m = 5		33 / 5 = 6	Reminder 3	smaller = 30	greater = 35

n = 84	m = 5		84 / 5 = 16 Reminder 4	smaller = 80	greaater = 85
'''

#!/bin/python

import os
import sys

#
# Complete the gradingStudents function below.
#


def gradingStudents(grades):
	roundedGrades = []
	for n in grades:
		m = 5
		reminder = n % m
		nextMultiple = m - reminder + n
		roundingResult = int(nextMultiple)-int(n)
		
		if roundingResult < 3 and nextMultiple >= 40 :
			roundedGrades.append(nextMultiple)
		else:
			roundedGrades.append(n)
		
	return roundedGrades


f = open('test.txt', 'w')

n = int(raw_input())

grades = []

for _ in xrange(n):
	grades_item = int(raw_input())
	grades.append(grades_item)

result = gradingStudents(grades)

f.write('\n'.join(map(str, result)))
f.write('\n')

f.close()
