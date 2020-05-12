N = 4
trust =[[1,3],[1,4],[2,3],[2,4],[4,3]]

import collections
judge = collections.defaultdict(list)
Njudge = collections.defaultdict(lambda : False)
for value in trust:
    a,b = value[0],value[1]
    Njudge[a] = True
    if not Njudge[b]:
        judge[b].append(a)

print(judge)
for i in judge.keys():
    if not Njudge[i] and len(judge[i]) == N-1:
        print(i)
        break
print(-1)