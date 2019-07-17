#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    for ind, val in enumerate(q):
        ind += 1
        if (val - ind > 2):
            print("Too chaotic")
            return

        compare = q[ind - 1]
        print(q[val-2:ind - 1])
        for i in q[max(val-2 , 0):ind - 1]:
            if (compare < i):
                count += 1

    print(count)
try:

except Exception as e

if __name__ == '__main__':
    # t = int(input())
    t = 1
    for t_itr in range(t):
        # n = int(input())
        #
        # q = list(map(int, input().rstrip().split()))
        q = [1, 2, 5, 3, 7, 8, 6, 4]
        # q = [2,1,5,3,4]
        minimumBribes(q)
