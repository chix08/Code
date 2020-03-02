t = int(input())
while t:
    t -= 1
    a, b, c, d = (map(int, input().split()))
    if a == b:
        print ('YES')
    else:
        if c == d:
            print ('NO')
        elif abs(a-b)%abs(c-d) == 0:
            print ('YES')
        else:
            print ('NO')