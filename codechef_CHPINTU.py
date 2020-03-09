t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    p = list(map(int, input().split()))
    cost = {}
    for f, p in zip(f, p):
        cost[f] = cost.get(f, 0) + p
    f = list(cost.values())
    f.sort()
    print(f[0])
