#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr: list, n: int) ->int:
    # Write your code here
    primary: list[int] = []
    secondary: list[int] = []
    for i, item in enumerate(arr):
        primary.append(arr[i][i])
        secondary.append(arr[i][n - i - 1])
        
    primary_sum, secondary_sum = 0, 0
    
    for i in range(n):
        primary_sum += primary[i]
        secondary_sum += secondary[i]
    return abs(primary_sum - secondary_sum)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n: int = int(input().strip())

    arr: list = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result: int = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
