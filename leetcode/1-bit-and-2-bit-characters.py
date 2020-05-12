bits = [1,0,0]

while len(bits):
    if len(bits) == 1 and bits[0] == 0:
        print(True)
    if bits.pop(0) == 1:
        bits.pop(0)
#--------------------------------------------------------

#----------------------------------------------------------

# matrix = [[0,0,0],[0,1,0],[0,0,1]]
# ans = [[0]*len(i) for i in matrix]
# visited = [[None]*len(i) for i in matrix]
# i = 0
# j = 0
# def findzero(i,j):
#     print()
#     if matrix[i][j] == 0:
#         return i + j
#     if j < len(matrix[i]) - 1 and visited[i][j+1] == None:
#         visited[i][j + 1] = 1
#         val = findzero(i,j+1)
#         ans[i][j] = abs(i + j - val)
#     if j > 0 and visited[i][j-1] == None:
#         visited[i][j-1] = 1
#         val = findzero(i,j-1)
#         ans[i][j] = abs(i + j - val)
#     if i > 0 and visited[i-1][j] == None:
#         visited[i - 1][j] = 1
#         val = findzero(i-1,j)
#         ans[i][j] = abs(i + j - val)
#     if i < len(matrix) - 1 and visited[i+1][j] == None:
#         visited[i + 1][j] = 1
#         val = findzero(i+1,j)
#         ans[i][j] = abs(i + j - val)
#
#     return val
#
#
# a = 0
# while a < len(matrix):
#    b = 0
#    while b < len(matrix[a]):
#        print(a,b)
#        if visited[a][b] == None:
#            findzero(2,2)
#        b += 1
#    a += 1
# # (findzero(0,0))
# print(ans)