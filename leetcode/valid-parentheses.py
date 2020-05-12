s = "{[]}"
d = {")": "(", "]": "[", "}": "{"}
stack = []
for i in s:
    if i in d.keys():
        if len(stack) > 0 and stack[-1] == d[i]:
            stack.pop()
        else:
            print(0)
    else:
        stack.append(i)

print(1)
