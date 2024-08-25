#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr: list[int]):
    # Write your code here
    n: int = len(arr)  # length of array
    # initialized counters
    positive: int = 0
    negative: int = 0
    zero: int = 0
    # traverse array and count positive, negative and zeroes
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        elif i == 0:
            zero += 1
        else:
            pass

    # perform ratios
    positive_ratio: float = float(positive/n)
    negative_ratio: float = float(negative/n)
    zero_ratio: float = float(zero/n)

    # print result upto 6 decimal places
    print(f"{positive_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
