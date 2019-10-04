ce = [0, 0, 0, 0, 0, 0]


def jumpingOnClouds(c):
    i = 0
    count = 0

    while (i <= len(c)):
        try:
            if (not c[i + 2]):
                i += 2
                count += 1
                continue
            if (not c[i + 1]):
                i += 1
                count += 1
                continue
        except Exception as e:
            break
    if(i == (len(c)-1)):
        print('count',count)
    else:
        count += 1
        print('count',count)

jumpingOnClouds(ce)