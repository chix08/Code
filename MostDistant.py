import math

def solve(coordinates):
    ans = -100000
    print(coordinates)
    for i in range(4):
        ix = coordinates[i][0]
        iy = coordinates[i][1]
        for j in coordinates[(i + 1):]:
            dx = j[0]
            dy = j[1]

            temp = ((dx - ix) * 2) + ((dy - iy) * 2)
            try:
                temp = math.sqrt(temp)
            except Exception as e:
                continue
            if(temp > ans):
                ans = temp
    print(ans)


a = [[-1, 0], [1, 0], [0, 1], [0, -1]]
solve(a)
