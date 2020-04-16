for _ in range(int(input())):
    n = int(input())
    d = n//2
    if d:
        print(d)
    else:
        print('1')
    if n == 1:
        print('1','1')
        continue
    if n == 2:
        print('2','1','2')
        continue
    # if n == 3:
    #     print('1',' ','1',' ','2',' ','3')
    else:
        print('3','1','2','3')
        i = 4
        while i < n:
            print('2',i,i+1)
            i += 2

        if i <= n:
            print('1',i)





