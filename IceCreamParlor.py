def whatFlavors(cost, money):
    # costdict = {}
    # newdict = {}
    # for index, value in enumerate(cost):
    #     if(not costdict.get(value)):
    #         costdict[value] = index + 1
    #     else:
    #         newdict[value] = index+1
    # for i in cost:
    #     try:
    #         minv = costdict[i]
    #         maxv = costdict[money - i]
    #         if(maxv != minv):
    #             print(minv, maxv)
    #         else:
    #             maxv = newdict[money - i]
    #             print(minv, maxv)
    #         return
    #     except Exception as e:
    #         continue

    map = {}
    for idx, val in enumerate(cost):
        residual = (money - val)
    if residual in map:
        print(sorted([map[residual], idx + 1]))
        break
    if not val in map:
        map[val] = idx + 1

# cost = [2,4,2,5, 3]
cost = [1, 2, 3, 5, 6]
money = 5
whatFlavors(cost, money)


map = {}
for idx, val in enumerate(cost):
residual = (money - val)
if residual in map:
print(sorted([map[residual], idx+1]))
break
if not val in map:
map[val] = idx+1