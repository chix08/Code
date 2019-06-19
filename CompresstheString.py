test = int(input())
while test:
    test -= 1
    n = int(input())
    s = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    temp = []
    # s[0] = s[0].upper()
    count = 0
    vol_c = True
    temp.append(s[0].upper())
    v = ''
    for i in s[1:]:
        if i not in vowels:
            v = ''
            count += 1
        else:
            if(count):
                temp.append(str(count))
            count = 0

            if v!=i:
                temp.append(i)
                v = i


    if(count):
        temp.append(str(count))
        print("".join(temp))
    else:
        print("".join(temp))

