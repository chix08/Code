import collections

def bfs(a):
    q = collections.deque()
    q.append(a)
    distance[a] = 0
    visited[a] = True
    while q:
        curr = q.popleft()
        for i in matrix[curr]:
            if not visited[i]:
                q.append(i)
                distance[i] = distance[curr] + 1
                visited[i] = True
    return


for _ in range(int(input())):
    n, q = map(int, input().split())
    visited = [False for _ in range(n + 1)]
    distance = [-1 for _ in range(n + 1)]
    check = collections.defaultdict(list)
    matrix = collections.defaultdict(list)
    for _ in range(q):
        a,x,b = map(str,input().split())
        a = int(a)
        b = int(b)
        if x == '=':
            matrix[a].append(b)
            matrix[b].append(a)
        else:
            check[a].append([a,b])

    c = False
    for v in check:
        if c:
            break
        ans = bfs(v[0])
        for e in check[v]:
            y,z = e[0],e[1]
            if distance[e[1]] != -1:
                c = True
                break
        visited = [False for _ in range(n + 1)]
        distance = [-1 for _ in range(n + 1)]
    if c:
        print('No')
    else:
        print('Yes')

