class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None



fir = Node(1)
sec = Node(2)
thi = Node(3)
fir.nextval = sec
sec.nextval = thi
temp = fir
s = ''
while(temp != None):
    print(temp.dataval)
    t = temp.dataval
    temp = temp.nextval
    s += str(t)
print(int(s))

