#SPOJ - Prime Path

import collections
import math

matrix = collections.defaultdict(list)
distance = [-1 for i in range(10000)]
visited = [False for j in range(10000)]
prime = []


def isPrime(i):
    j = 2
    while j < math.sqrt(i) + 1:
        if i % j == 0:
            return False
        j += 1
    return True


for i in range(1001, 10000, 2):
    if isPrime(i):
        prime.append(i)
print()


def isValid(first, second):
    cnt = 0
    first = str(first)
    second = str(second)
    for i in range(4):
        if first[i] != second[i]:
            cnt += 1
    if cnt == 1:
        return True
    return False


def createGraph():
    for i, v in enumerate(prime):
        for j in prime[i:]:
            if isValid(v, j):
                matrix[v].append(j)
                matrix[j].append(v)


createGraph()


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


for _ in range(int(input())):
    a, b = map(int, (input().split()))
    distance = [-1 for i in range(10000)]
    visited = [False for j in range(10000)]
    bfs(a)
    print(distance[b])
