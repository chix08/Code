def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    ans = a*b
    hcf = gcd(a,b)
    lcm = ans // hcf
    print(hcf,' ',lcm)