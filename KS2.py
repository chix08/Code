p = int(input())
for i in range(p):
    num = input()
    sum1 = 0
    for i in range(len(num)):
        sum1+=int(num[i])
    for i in range(10):
        if (sum1+i)%10==0:
            num=num+str(i)
    print(num)

