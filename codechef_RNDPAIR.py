from collections import Counter
t = int(input())
while t:
    t -= 1
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    d = Counter(l)
    print(d)
    pass
    if l[-1] == l[-2]:
        s = (d[l[-1]] * (d[l[-2]] - 1)) / 2
    else:
        s = (d[l[-1]] * (d[l[-2]]))

    p = n * (n - 1) / 2
    j = (s / p)
    print("{0:.8f}".format(j))
