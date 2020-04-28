s = "011100"
i = 0
j = len(s)-1
maxans = 0
suffix = [0]
prefix = [0]
while i < len(s)-1:
    if s[i] == '0':
        suffix.append(suffix[i]+1)
    else:
        suffix.append(suffix[i])

    if s[j] == '1':
        prefix.append(prefix[i]+1)
    else:
        prefix.append(prefix[i])

    i += 1
    j -= 1
# print(suffix)
# print(prefix)
j += 1
while j < len(s):
    tans = prefix[i] + suffix[j]
    if maxans < tans:
        maxans = tans
    j += 1
    i -= 1
print(maxans)

