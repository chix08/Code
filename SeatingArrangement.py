i = int(input())
a = (i%12)*2
if(a!=0):
    seat = 13 - a
else:
    seat = -11
print(i + seat)
