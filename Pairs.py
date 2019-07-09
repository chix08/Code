#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the pairs function below.
def pairs(k, arr):
    count = 0
    for i in arr:
        try:
            c = cd.get(i + k)
            count += c
        except:
            continue
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))
    cd = {}
    for i in arr:
        cd[i] = cd.get(i, 0) + 1

    arr = set(arr)

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
