
s =  "a)b(c)d"
stack = []
s = list(s)
for i,v in enumerate(s):
    if v == ')' and not len(stack):
        s[i] = ''
    elif v == ')':
        stack.pop()
    elif v == '(':
        stack.append(i)

for v in stack:
    s[v] = ''
s = ''.join(s)
print(s)
