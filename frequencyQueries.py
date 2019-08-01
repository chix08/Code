def freqQuery(queries):
    d = {}
    a = []
    check = {}
    for q in queries:
        oldKey = 0
        newKey = 0
        done = True
        print(q)
        if q[0] == 1:
            try:
                oldKey = d[q[1]]
                check[oldKey].remove('True')
                d[q[1]] += 1
                newKey = d[q[1]]
                check[newKey] = check.get(newKey, [])
                check[newKey].append('True')
            except:
                d[q[1]] = 1
                newKey = 1
                check[newKey] = check.get(newKey, [])
                check[newKey].append('True')
        elif q[0] == 2:
            try:
                oldKey = d[q[1]]
                check[oldKey].remove('True')
                d[q[1]] -= 1
                newKey = d[q[1]]
                check[newKey].append('True')
            except:
                continue
        else:
            try:
                if True in check[q[1]]:
                    a.append('1')
                else:
                    a.append('0')
            except:
                a.append('0')
    return a




queries = [[1, 5], [1, 6], [1, 5], [1, 6], [2, 5], [2, 5], [2 ,5] , [2,6],[2,6]]
ans = freqQuery(queries)
