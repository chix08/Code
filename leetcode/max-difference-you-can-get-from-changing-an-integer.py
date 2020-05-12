
def createMax(num):
    result = ''
    lnum = list(str(num))
    replaceValue = '-1'
    for index,value in enumerate(lnum):
        if value != '9':
            replaceValue = value
            lnum[index] = '9'
            break
    ans = ''.join(lnum)
    ans = ans.replace(replaceValue,'9')
    return int(ans)


def createMin(num):
    lnum = list(str(num))
    i = 0
    while i < len(lnum) - 1:
        if lnum[i] == '1' or lnum[i]=='0':
            i += 1
        else:
            break   
    if lnum[i] == lnum[0]:
        ans = ''.join(lnum)
        ans = ans.replace(lnum[i],'1')
    else:
        ans = ''.join(lnum)
        ans = ans.replace(lnum[i],'0')
        
    return int(ans)


num = 1101057
print(createMax(num))
print(createMin(num))
result = createMax(num) - createMin(num)
print(result)
