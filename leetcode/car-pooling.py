result = {}
seats = 0
trips = [[1,12,7],[3,7,9],[8,3,9]]
capacity = 11
for i in trips:
    result[i[1]] = result.get(i[1],0) + i[0]
    result[i[2]] = result.get(i[2],0) - i[0]

# print(result)
for i in range(1,1001):
    seats += result.get(i,0)
    if seats > capacity:
        print(0)
        exit()
print(1)

