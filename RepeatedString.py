#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = n // len(s)
    a = n-(len(s)*l)
    ca = [0]
    count = 0
    for i in s:
        if(i == 'a'):
            count += 1
        ca.append(count)
    count = ca[a]+(count*l)
    return count
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
s = input()
#
n = int(input())
#
result = repeatedString(s, n)
print(result)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
