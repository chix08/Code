from sys import stdin as s
from sys import stdout


def solve(k, l, r, li, val):
    ans = 0
    if val % 2 == 0:
        ans = li[r - 1] - li[l - 1] + 1
    else:
        ans = li[r - 1] - li[l - 1]
    if k == 0:
        return ans
    else:
        return r - l + 1 - ans


def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a);


def elim(m, n):
    d = gcd(m, n)
    num = int(m / d)
    den = int(n / d)
    return [num, den]


allans = []
t = int(s.readline())
for _ in range(t):
    n, q = map(int, s.readline().split(" "))
    li1 = [int(x) for x in s.readline().strip().split(" ")]
    li2 = []
    count = 0
    for i in li1:
        if i % 2 == 0:
            count += 1
        li2.append(count)
    for i in range(q):
        k, l, r = [int(x) for x in s.readline().split(" ")]
        ans = solve(k, l, r, li2, li1[l - 1])
        if ans == 0 or ans == r - l + 1:
            allans.append("{}\n".format(int(ans / (r - l + 1))))
        else:
            ans = elim(ans, r - l + 1)
            allans.append("{} {}\n".format(ans[0], ans[1]))
allans = ''.join(allans)
stdout.write(allans)