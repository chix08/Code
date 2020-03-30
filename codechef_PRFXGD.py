for _ in range(int(input())):
    s = list(input())
    k,x = map(int,input().split())
    kate = 0
    count = 0
    sno = {}
    for i in s:
        sno[i] = sno.get(i,0)+1
        if sno[i] <= x:
            count += 1
            continue
        if sno[i] > x and kate < k:
            kate += 1
        else:
            break
    print(count)
