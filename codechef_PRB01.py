import math

pl = [1] * 100000

i = 3
while i < math.sqrt(len(pl)):
    # print('--> ', i, ' Is prime')
    j = i * i
    while j < len(pl):
        pl[j] = 0
        j += i
    i += 2

t = int(input())
while t:
    t -= 1
    num = int(input())
    if pl[num] and (num % 2 == 1 or num == 2):
        print('yes')
    else:
        print('no')
