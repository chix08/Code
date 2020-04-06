import math as mt

MAXN = 100001

spf = [0 for i in range(MAXN)]

def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, mt.ceil(mt.sqrt(MAXN))):
        if (spf[i] == i):
            for j in range(i * i, MAXN, i):
                if (spf[j] == j):
                    spf[j] = i



def getFactorization(x):
    # ret = list()
    d = dict()
    while (x != 1):
        d[spf[x]] = d.get(spf[x],0)+1
        # ret.append(spf[x])
        x = x // spf[x]

    return d

sieve()
factor = {}
for x in range(1,10001):
    factor[x]=getFactorization(x)
# print(factor)

# l = [2,4,5,10,45]
for i in range(int(input())):
    n , m = map(int,input().split())
    l = list(map(int, input().split()))
    curlcm = 1
    lcm = {}
    # l = [2,5,6,3]
    for i in l:
        for j in factor[i]:
            try:
                if lcm[j] >= factor[i][j]:
                    continue
                else:
                    t = lcm[j]
                    lcm[j] = factor[i][j]
                    curlcm *= j*(factor[i][j]-t)
            except KeyError:
                lcm[j] = factor[i][j]
                curlcm *= j * factor[i][j]
    # print(curlcm)
    maxlcm = curlcm
    index = 1
    for i in range(1,m+1):
        dc = curlcm
        for j in factor[i]:
            try:
                if lcm[j] >= factor[i][j]:
                    continue
                else:
                    t = lcm[j]
                    lcm[j] = factor[i][j]
                    dc *= j ** (factor[i][j] - t)
            except KeyError:
                f = True
                dc *= j ** factor[i][j]
        if maxlcm < dc:
            maxlcm = dc
            index = i
    print(index)
