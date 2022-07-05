#!/bin/python3

import math
import os
import random
import re
import sys

from IndexErrorPack import find_index_error

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def make_string():
    return ""

def fab_row(n, i, string):
    string += " " * (n - i)
    string += "#" * i
    string += "\n"
    if i == n:
        return string
    else:
        return fab_row(n, i + 1, string)

def staircase(n):
    matrix = fab_row(n, 1, make_string())

    print(matrix)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
