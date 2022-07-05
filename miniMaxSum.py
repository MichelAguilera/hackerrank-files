#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def getMinSum(numbers):
    zum = 0
    for n in numbers:
        zum += n
    return zum

def getMaxSum(numbers):
    zum = 0
    for n in numbers:
        zum += n
    return zum

def miniMaxSum(arr):
    nbrs = sorted(arr)

    min_s = getMinSum(nbrs[ :-1])
    max_s = getMaxSum(nbrs[1:  ])
    print(min_s, max_s)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)