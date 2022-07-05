# https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

class Hourglass:

    def setDimensions(origin, **kwargs):
        if kwargs['i'] != None:
            i = kwargs['i']
        else:
            i = 0

        return [
            (origin[0 + i], origin[1 + i]),     (origin[0 + i] + 1, origin[1 + i]),     (origin[0 + i] + 2, origin[1 + i])      , 
                                                (origin[0 + i] + 1, origin[1 + i]) + 1                                          , 
            (origin[0 + i], origin[1 + i]) + 2, (origin[0 + i] + 1, origin[1 + i]) + 2, (origin[0 + i] + 2, origin[1 + i]) + 2
        ]

    def __init__(self, origin):
        self.dimensions = self.setDimensions(origin)

    def totalSum(self, matrix):
        zum = 0
        for i in self.dimensions:



def hourglassSum(arr):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
