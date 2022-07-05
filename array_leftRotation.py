# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rotLeft(a, d):
    a1 = a.copy()
    for i in range(len(a)):
        # print(a, a1)
        a1[i] = a[(i + d) % len(a)]
        # print(f"Setting index of a1[{i}] to a[{(i + d) % len(a)}] :: {a1[i]} == {a[(i + d) % len(a)]}")
    return a1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # d = int(first_multiple_input[1])

    # a = list(map(int, input().rstrip().split()))

    # result = rotLeft(a, d)
    a = [1, 2, 3, 4, 5]
    d = int(input("how many times"))
    test = rotLeft(a, d)
    print(test)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
