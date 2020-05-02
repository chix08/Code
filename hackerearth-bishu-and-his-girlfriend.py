n = int(input())
matrix ={}
for _ in range(1,n):
    a,b = map(int, input().split())
    if matrix.get(a,0):
        matrix[a].append(b)
    else:
        matrix[a] = [b]
    if matrix.get(b, 0):
        matrix[b].append(a)
    else:
        matrix[b] = [a]
gl = []
q = int(input())
for _ in range(q):
    gl.append(int(input()))
visited = [False for _ in range(1,n+2)]
distance = [0 for _ in range(1,n+2)]
# print(matrix)
def dfs(i,count):
    for p in matrix[i]:
        if not visited[p]:
            visited[p] = True
            distance[p] = dfs(p,count+1)
    return count
visited[1] = True
dfs(1,0)
# print()

mindist = 999999
girl = 999999
for i in gl:
    if distance[i]<=mindist:
        if mindist == distance[i] and i > girl:
            pass
        else:
            girl = i
        mindist = distance[i]


print(girl)