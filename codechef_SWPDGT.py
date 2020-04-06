# def num(n):
#   l = []
#   n = int(n)
#   while n:
#     l.append(n%10)
#     n = n//10
#   # if len(l) == 1:
#   #   l.append(0)
#   l.sort()
#   return l
# for _ in range(int(input())):
#   a , b = map(int, input().split())
#   if a < 10 and b < 10:
#     print(a+b)
#   else:
#     maxsum = a + b
#     la = num(a)
#     lb = num(b)
#     # print(la)
#     # print(lb)
#     sa = 0
#     sb = int(str(max(la[-1], lb[-1])) + str(min(la[-1], lb[-1])))
#     if len(lb)>1 and len(la) > 1:
#       sa = int(str(max(la[0],lb[0])) + str(min(la[0],lb[0])))
#       print(max(sa + sb,maxsum))
#       continue
#     if len(la) > 1:
#       sa = int(la[0])
#     if len(lb) > 1:
#       sa = int(lb[0])
#     print(max(sa + sb,maxsum))


for _ in range(int(input())):
    a, b = input().split()
    maxsum = int(a) + int(b)
    a = list(map(int, list(a)))
    b = list(map(int, list(b)))
    a.sort(reverse=True)
    b.sort(reverse=True)
    ans = -1
    if len(a) <= 1 and len(b) <= 1:
        ans = a[0] + b[0]
    if len(a) > 1 and len(b) <= 1:
        ans = int(str(max(a[0],b[0])) + str(min(a[0],b[0]))) + a[1]
    if len(b) > 1 and len(a) <= 1:
        ans = int(str(max(a[0],b[0])) + str(min(a[0],b[0]))) + b[1]
    if len(a) > 1 and len(b) > 1:
        ans = int(str(max(a[0],b[0])) + str(min(a[0],b[0]))) + int(str(max(a[1],b[1])) + str(min(a[1],b[1])))

    print(max(maxsum, ans))
