for _ in range(int(input())):
    # n = int(input())
    l = list(map(int, input().split()))
    i = 0
    f = True
    while i < len(l) and f:
        if l[i]:
            i += 1
            count = 0
            while i <= (len(l)-1) and l[i] == 0:
                i += 1
                count += 1

            if i <= (len(l) - 1) and count >= 5:
                continue

            if i <= (len(l) - 1) and count < 5:
                f = False
                break

        else:
            i += 1
    if f:
        print('YES')
    else:
        print('NO')



