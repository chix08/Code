import collections
# hasApple = [0,0,1,0,1,1,0]
hasApple = [0,0,0,0,0,0,0,1,0]
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6],[4,7],[4,8]]
n = 9
# visited = [False * i for i in range(n)]
# foundApple = [False * i for i in range(n)]
# path = collections.defaultdict(list)
# for i in edges:
#     path[i[0]].append(i[1])
#     path[i[1]].append(i[0])
# ans = 0
# def dfs(node,parent,ans):
#     for i in path[node]:
#         if not visited[i]:
#             visited[i] = True
#             p = node
#             ans = dfs(i,p,ans)
#             if foundApple[p] and foundApple[i]:
#                 ans += 2
#
#
#     if hasApple[node] or foundApple[node]:
#         foundApple[parent] = True
#         foundApple[node] = True
#     return ans
#
# visited[0] = True
#
# print(dfs(0,0,ans))
# # print(visited)
#

class Solution:
    def minTime(self, n, edges, hasApple) -> int:
        tree = [[] for _ in range(n)]
        for f, t in edges:
            tree[f].append(t)
            tree[t].append(f)

        # Return a the number of steps to reach all apples and come back
        # to the current node. Return 0 if no apples found.
        def dfs(parent, node):
            steps = 0
            for c in tree[node]:
                if c != parent:
                    steps += dfs(node, c)
            if (hasApple[node] or steps > 0) and node != 0:
                steps += 2
            return steps

        return dfs(-1, 0)
s = Solution()
s.minTime(n,edges,hasApple)