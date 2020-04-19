for _ in range(int(input())):
    n = int(input())
    lon = list(map(int,input().split()))
    count = 0
    series = []
    total = (n*(n+1))//2
    for i in lon:
        if i % 2 == 1:
            series.append(0)
            continue
        if i % 4 == 0:
            series.append(2)
            continue
        else:
            series.append(1)
    d = {0: 1}
    sum = 0
    k = 1
    for i in series:
        sum += i
        if d.get(sum - k):
            count += d.get(sum - k)
        d[sum] = d.get(sum, 0) + 1


    print(total-count)







