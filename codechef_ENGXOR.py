# cook your dish here
from sys import stdin, stdout
t=int(input())
for _ in range(t):
    number,nopfp=map(int,stdin.readline().split())
    odd=0
    even=0
    nums=list(map(int,stdin.readline().split()))
    for num in nums:
        value=(bin(num).count("1"))
        if value%2==0:
            even+=1
        else:
            odd+=1
    print(nums)

    while nopfp:
        nopfp -= 1
        val = int(stdin.readline())
        pairity=(bin(val).count("1"))
        if(pairity%2):
            stdout.write(str(odd)+" "+str(even))

        else:
            stdout.write(str(even)+" "+str(odd))
            stdout.write("\n")