'''
k = Range
n = length
arr = array
'''

arr = [9,8,7,6,5,4,3,2,1,0]


def sortarray(acount, actualarr, n):
    a = [0 for i in range(n)]
    for i in actualarr:
        a[acount[i] - 1] = i
        acount[i] -= 1

    return a


def countnum(k, arr):
    a = [0 for i in range(k)]
    for i in arr:
        a[i] = a[i] + 1

    for i in range(k - 1):
        a[i + 1] = a[i] + a[i + 1]

    b = sortarray(a, arr, len(arr))
    return b


length = len(arr)
k = 10
b = countnum(k, arr)
print(b)
