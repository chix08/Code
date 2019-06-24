import array as ar
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

import numpy as np
temp_list = list(map(int,(input().split())))
arr = np.array(temp_list)










#
# test = int(input())
# while test:
#     test -= 1
#     n, q = map(int, (input().split()))
#     arr = ar.array('L', (map(int, (input().split()))))
#     while q:
#         q -= 1
#         k, l, r = map(int, (input().split()))
#         l -= 1
#         even = 0
#         for i in range(l, r):
#             if arr[i] % 2 == 0:
#                 even += 1
#         if k:
#             if (r - l - even):
#                 b = gcd((r - l - even), (r - l))
#                 print(int((r - l - even) / b), int((r - l) / b))
#             else:
#                 print('0')
#
#         else:
#             if even:
#                 b = gcd(even, (r - l))
#                 print(int(even / b), int((r - l) / b))
#
#             else:
#                 print('0')
#
