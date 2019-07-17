#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(a):
    i = 0
    j = 0
    max1 = -1000000
    while(i < 4):
        j = 0
        while(j < 4):
            sum1 = a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
            print(sum1)
            if(sum1 > max1):
                max1 = sum1
            j += 1
        i += 1
    return max1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
