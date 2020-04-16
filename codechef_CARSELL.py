for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    print(l)
    m = 1000000007
    c = 0
    price = 0
    for i in l:
        tp = i - c
        if tp > 0:
            price += tp
            c += 1
        else:
            break
    print(price%m)



