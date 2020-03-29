M = 10 ** 9 + 7
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    count = 0
    f = 0
    for i in range(1, n):
        if l[i] < l[i - 1]:
            f = 1
            break
        x = bin(l[i] & l[i - 1])
        count = count + x.count('1')
        # print(count)
    if f:
        print('0')
        continue
    print((2 ** count) % M)
