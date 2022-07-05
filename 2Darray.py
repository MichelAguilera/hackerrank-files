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

    def __init__(self, matrix, origin):
        self.matrix = matrix
        self.origin = origin

    def setDimensions(self):
        return [
            (0 + self.origin[0], 0 + self.origin[1]), (0 + self.origin[0], 1 + self.origin[1]), (0 + self.origin[0], 2 + self.origin[1]), 
                                                      (1 + self.origin[0], 1 + self.origin[1]),
            (2 + self.origin[0], 0 + self.origin[1]), (2 + self.origin[0], 1 + self.origin[1]), (2 + self.origin[0], 2 + self.origin[1])
        ]

    def totalSum(self):
        z = 0
        for tuple in self.setDimensions():
            z += self.matrix[tuple[0]][tuple[1]]
        print(self.matrix, z)
        return z

def hourglassSum(arr):
    res = []
    h = Hourglass(arr, (0, 0))
    for y in range(4):
        for x in range(4):
            res.append(h.totalSum())
            h.origin = (y, x)

    print(res)
    return max(res)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))

    # result = hourglassSum(arr)
    matr = [
        [3, 7, -3, 0, 1, 8],
        [1, -4, -7, -8, -6, 5],
        [-8, 1, 3, 3, 5, 7],
        [-2, 4, 3, 1, 2, 7],
        [2, 4, -5, 1, 8, 4],
        [5, -7, 6, 5, 2, 8]
    ]
    test = hourglassSum(matr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
