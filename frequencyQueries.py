def freqQuery(queries):
    d = {}
    check = {}
    oldkey = 0
    newkey = 0
    for q in queries:
        try:
            if q[0] == 1:
                try:
                    oldkey = d[q[1]]
                except:
                    oldkey = 0
                d[q[1]] = d.get(q[1], 0)+1
                newkey = d[q[1]]

            elif q[0] == 2:
                d[q[1]] -= 1
            else:
                print(d[q[1]])
        except Exception as e:
            print(e)
    return
















    # di = {}
    # a = []
    # check = []
    # for q in queries:
    #     done = True
    #     try:
    #         if q[0] == 1:
    #             di[q[1]] = di.get(q[1], 0)+1
    #         elif q[0] == 2:
    #             di[q[1]] = di[q[1]] - 1
    #         else:
    #             for ch in di.values():
    #                 if ch == q[1]:
    #                     a.append('1')
    #                     done = False
    #                     break
    #             if(done):
    #                 a.append('0')
    #
    #     except:
    #         print('EXCEPTION')
    # print(a)


queries = [[1, 5], [1, 6], [2, 7], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]]
ans = freqQuery(queries)
