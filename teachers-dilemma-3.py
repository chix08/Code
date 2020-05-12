# c = 0
def find(v):

    if parent[v] < 0:
        return v
    else:
        x = find(parent[v])
        parent[v] = x
        return x


def union(a, b):
    parent[a] += parent[b]
    parent[b] = a


n, m = map(int, input().split())
parent = [-1 for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    a = find(a)
    b = find(b)
    if a != b:
        union(a, b)
res = 1
# print(parent)
for i in parent:
    if i < 0:
        res = (res * abs(i)) % 1000000007
print(res)