#!/bin/python

import sys


def camelcase(s):
    wordsCounter = 0

    for index, value in enumerate(s):
        if index == 0:
            wordsCounter += 1

        if not value.islower():
            wordsCounter += 1

    return wordsCounter


if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
