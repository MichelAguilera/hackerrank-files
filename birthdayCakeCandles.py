# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_num = max(candles)
    tall_count = 0
    for candle in candles:
        if candle == max_num:
            tall_count += 1
    return tall_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    # candles = [10, 2, 3, 10, 10, 3, 10]
    result = birthdayCakeCandles(candles)
    # print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
