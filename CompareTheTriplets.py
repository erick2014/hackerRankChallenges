#!/bin/python

import sys


def solve(a0, a1, a2, b0, b1, b2):
    points = []

    if a0 > b0 or a0 > b1 or a0 > b2 or a2 > b0 or a2 > b2:
        points.append(1)
    else:
        points.append(0)

    if a0 < b0 or a0 < b1 or a0 < b2 or a2 < b0 or a2 < b2:
        points.append(1)
    else:
        points.append(0)

    return points


a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]

b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
