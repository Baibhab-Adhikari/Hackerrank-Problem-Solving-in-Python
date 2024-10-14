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


def miniMaxSum(arr) -> None:
    # Write your code here

    # init all the required variables

    total: int = 0
    arr2: list[int] = []  # empty list for storing all the totals
    size: int = len(arr)

    # calculating the total of all the elements in the array

    for i in arr:
        total += i

    # calculating the sum of all elements except one element in the array
    for j in range(size):
        total2: int = total - arr[j]
        arr2.append(total2)

    # print the maximum and minimum of the sums stored in the new array

    print(min(arr2), max(arr2))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
