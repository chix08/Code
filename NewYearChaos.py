# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    a = [i for i in range(1, len(q) + 1)]
    print(a)
    for j, i in zip(q, a):
        print(i, j)
        if (j - i > 2):
            return ('Too chaotic')
        if (j - i > 0):
            count = count + (j - i)
    print(count)
    return count


t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)
