T = [73, 74, 75, 71, 69, 72, 76, 73]
ans = [0] * len(T)
stack = []

for i in range(len(T)-1,-1,-1):
    while stack:
        if T[i] < stack[-1][0]:
            ans[i] = stack[-1][1] - i
            break
        else:
            stack.pop()
    stack.append([T[i],i])
print(ans)
