#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    count = len(arr) - 1
    arr.sort()
    first = 0
    second = 1
    diff = 99999999
    while second < (len(arr)):
        # print('first',arr[first])
        # print('second',arr[second])
        temp = abs(arr[first] - arr[second])

        if (temp < diff):
            temp, diff = diff, temp
        first += 1
        second += 1
    return diff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
