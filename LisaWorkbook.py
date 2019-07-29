import math


def workbook(n, k, arr):
    page = 0
    count = 0
    pageinc = True
    for i in arr:
        if(pageinc):
            page += 1
        for j in range(1, i + 1):
            if j % k == 0:
                if (j == page):
                    count += 1
                # print(j, 'Page', page)
                page += 1
                pageinc = False
            else:
                if (j == page):
                    count += 1
                # print(j, 'Page', page)
                pageinc = True
    return count


n = 5
k = 3
arr = [4, 2, 6, 1, 10]
result = workbook(n, k, arr)
print(result)
