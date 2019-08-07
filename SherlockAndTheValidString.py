def isValid(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    check = list(d.values())
    i = 0
    extra = 2
    l = len(check)
    allow = check[0]
    while extra and i < l:
        if(check[i] == allow):
            i += 1
        elif abs(check[i]-allow) == 1:
            extra -= 1
            i += 1
        else:
            return 'NO'
    if extra:
        return 'YES'
    else:
        return 'NO'

s = 'abcdefghhgfedecba'


result = isValid(s)
print(result)
