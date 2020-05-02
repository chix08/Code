n, e = map(int, input().split())
matrix = {}
visited = [False for i in range(1,n+2)]
for i in range(e):
    a,b = map(int, input().split())
    if matrix.get(a,0):
        matrix[a].append(b)
    else:
        matrix[a] = [b]
    if matrix.get(b, 0):
        matrix[b].append(a)
    else:
        matrix[b] = [a]
print(matrix)

def dfs(i):
    try:
        for p in matrix[i]:
            if not visited[p]:
                visited[p] = True
                dfs(p)
    except KeyError:
        return
    return

i = 1
count = 0
while i < len(visited):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        count += 1
    i += 1
print(count)