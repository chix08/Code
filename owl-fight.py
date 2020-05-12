def find(v):
    if v == parent[v]:
        return v
    else:
        # x = find(parent[v])
        # parent[v] = x
        # return x
        return find(parent[v])

def union(a, b):
    if a < b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    a = find(u)
    b = find(v)
    if a != b:
        union(a, b)

for _ in range(int(input())):
    u, v = map(int, input().split())
    a = find(u)
    b = find(v)
    if a == b:
        print('TIE')
    elif a>b:
        print(u)
    else:
        print(v)



