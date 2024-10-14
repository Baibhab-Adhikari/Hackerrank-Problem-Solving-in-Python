#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#


def staircase(n):
    # Write your code here
    # loop for the pattern printing
    for i in range(n):
        # space will be printed from 0 to n-i-1 for each row
        # # will be printed from 0 to i+1 for each row
        print(" "*(n-i-1), end="")  # print the spaces in the same line
        print("#"*(i + 1))  # print the hash with nextline


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
