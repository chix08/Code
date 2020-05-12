image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
maxi = len(image) - 1
maxj = len(image[0])-1
directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
visited = [[False for i in range(len(image[0]))] for t in range(len(image))]

def fill(i, j, newColor, changeColor):
    for t in directions:
        a, b = i + t[0], j + t[1]
        if 0 <= a <= maxi and 0 <= b <= maxj and not visited[a][b]:
            print(a,b)
            if image[a][b] == changeColor:
                visited[a][b] = True
                image[a][b] = newColor
                fill(a, b, newColor, changeColor)
    image[i][j] = newColor

visited[sr][sc] = True
fill(sr, sc, newColor, image[sr][sc])
print(image)
