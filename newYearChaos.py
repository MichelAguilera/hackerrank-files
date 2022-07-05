# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
from pickle import FALSE
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def checkOrder(arr, index):
    if arr[index] + arr[index + 1] == arr[index] + 1:   return False
    else:                                               return True

def isChaotic(arr, index):
    m = []
    for n in arr[index-2:index+3]:
        if n == arr[index]:
            if arr[index] == arr[- 2]: break
            continue
        else: 
            m.append(n)
    if (
       (arr[index] - 2 not in m or
        arr[index] - 1 not in m or
        arr[index] + 1 not in m or
        arr[index] + 2 not in m) and m != []
    ):
        print(m)
        return True
    else: return False

def minimumBribes(q):
    bribes = 0
    for i in range(len(q) - 1): # LOOP THROUGH ALL VALUES OF q
        if isChaotic(q, i): # Check for chaos
            print("Too Chaotic")
            break
        if checkOrder(q, i): # Check for numbers out of order
            bribes += 1


if __name__ == '__main__':
    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     q = list(map(int, input().rstrip().split()))

        # minimumBribes(q)

    q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    minimumBribes(q)
