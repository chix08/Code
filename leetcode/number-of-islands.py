# grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]
# grid = [['1','0','1','0'],['0','0','0','0'],['1','0','1','0'],['0','0','0','0']]
# grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
grid = [["0","0","0","0","0"],["1","1","0","0","0"],["0","0","0","0","0"],["0","0","0","1","1"]]

visited = [[False]*len(i) for i in grid]
Maxi = len(grid)
Maxj = len(grid[0])
def TreeTraversal(i,j):
    if i < Maxi - 1 and not visited[i+1][j]:
        visited[i+1][j] = True
        if grid[i+1][j] == '0':
            visited[i+1][j] = False
        else:
            TreeTraversal(i+1,j)

    if i > 0 and not visited[i-1][j]:
        visited[i-1][j] = True
        if grid[i-1][j] == '0':
            visited[i-1][j] = False
        else:
            TreeTraversal(i-1,j)

    if j < Maxj - 1 and not visited[i][j+1]:
        visited[i][j+1] = True
        if grid[i][j+1] == '0':
            visited[i][j+1] = False
        else:
            TreeTraversal(i,j+1)

    if j > 0 and not visited[i][j-1]:
        visited[i][j-1] = True
        if grid[i][j-1] == '0':
            visited[i][j-1] = False
        else:
            TreeTraversal(i,j-1)

    return
count = 0
for i in range(0,len(grid)):
    for j in range(0,len(grid[i])):
        if grid[i][j] != '0' and not visited[i][j]:
            visited[i][j] = True
            TreeTraversal(i,j)
            count += 1

print(count)


# #Good Approach
#
# def is_valid(self, grid, r, c):
#     m, n = len(grid), len(grid[0])
#     if r < 0 or c < 0 or r >= m or c >= n:
#         return False
#     return True
#
#
# def numIslandsDFS(self, grid):
#     """
#     :type grid: List[List[str]]
#     :rtype: int
#     """
#     if not grid or not grid[0]:
#         return 0
#
#     m, n = len(grid), len(grid[0])
#     count = 0
#     for i in xrange(m):
#         for j in xrange(n):
#             if grid[i][j] == '1':
#                 self.dfs(grid, i, j)
#                 count += 1
#     return count
#
#
# def dfs(self, grid, r, c):
#     grid[r][c] = '0'
#     directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#     for d in directions:
#         nr, nc = r + d[0], c + d[1]
#         if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
#             self.dfs(grid, nr, nc)